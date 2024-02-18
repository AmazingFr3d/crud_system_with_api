from flask import render_template, flash, redirect, url_for, request
from sqlalchemy import or_, desc
from flask_login import login_required
import pandas as pd
from datetime import datetime

import traceback

from . import main_bp
from .forms import *
from .models import *
from .dash_helpers import dash_embeds as de
from .upload_helper import upload_map as um

per_page = 50


@main_bp.route('/members', methods=['GET', 'POST'])
@login_required
def members():
    page = request.args.get('page', 1, type=int)
    data_set = Members.query.paginate(page=page, per_page=per_page)
    return render_template('tables/members.html', data_set=data_set, db="members")


@main_bp.route('/leads', methods=['GET', 'POST'])
@login_required
def leads():
    page = request.args.get('page', 1, type=int)
    data_set = Leads.query.paginate(page=page, per_page=per_page)
    count = Leads.query.count()
    return render_template('tables/leads.html', data_set=data_set, db="leads", count=count)


@main_bp.route('/transactions', methods=['GET', 'POST'])
@login_required
def transactions():
    form = TransactionForm()
    if form.is_submitted():
        if form.type.data == 'all':
            page = request.args.get('page', 1, type=int)
            data_set = Transactions.query.paginate(page=page, per_page=per_page)
            count = Transactions.query.count()
            return render_template('tables/transactions.html', data_set=data_set, db="All Transactions", form=form,
                                   count=count)

        elif form.type.data == 'sales':
            page = request.args.get('page', 1, type=int)

            data_set = Transactions.query.filter(or_(Transactions.transaction_type == "Sale")).paginate(page=page,
                                                                                                        per_page=per_page)
            count = Transactions.query.filter(or_(Transactions.transaction_type == "Sale")).count()
            return render_template('tables/transactions.html', data_set=data_set, db="Sales", form=form, count=count)

        elif form.type.data == 'refunds':
            page = request.args.get('page', 1, type=int)

            data_set = Transactions.query.filter(or_(Transactions.transaction_type == "Refund",
                                                     Transactions.transaction_type == "Chargeback")).paginate(page=page,
                                                                                                              per_page=per_page)
            count = Transactions.query.filter(or_(Transactions.transaction_type == "Refund",
                                                  Transactions.transaction_type == "Chargeback")).count()
            return render_template('tables/transactions.html', data_set=data_set, db="Refunds", form=form, count=count)
    else:
        page = request.args.get('page', 1, type=int)
        data_set = Transactions.query.paginate(page=page, per_page=per_page)
        count = Transactions.query.count()
        return render_template('tables/transactions.html', data_set=data_set, db="All Transactions", form=form,
                               count=count)


@main_bp.route('/summary', methods=['GET', 'POST'])
@login_required
def summary():
    form = SumForm()
    try:
        if form.is_submitted():
            freq = form.freq.data
            if freq == "monthly":
                sales = Transactions.query.filter(or_(Transactions.transaction_type == "Sale")).all()
                sales_df = pd.DataFrame(
                    [{'Date': trans.transaction_date, "Amount": trans.amount, "Count": trans.product} for trans in
                     sales])
                sales_df.Date = pd.to_datetime(sales_df.Date)
                sales_df.set_index('Date', inplace=True)
                sales_df = sales_df.resample('MS').agg({"Amount": "sum", "Count": "count"})
                sales_df = sales_df.sort_index(ascending=False)

                refund = Transactions.query.filter(or_(Transactions.transaction_type == "Refund",
                                                       Transactions.transaction_type == "Chargeback")).all()
                refund_df = pd.DataFrame(
                    [{'Date': trans.transaction_date, "Amount": trans.amount, "Count": trans.product} for trans in
                     refund])
                refund_df.Date = pd.to_datetime(refund_df.Date)
                refund_df.set_index('Date', inplace=True)
                refund_df = refund_df.resample('MS').agg({"Amount": "sum", "Count": "count"})
                refund_df = refund_df.sort_index(ascending=False)

                return render_template('dash/summary.html', sales=sales_df, refunds=refund_df, db="transactions",
                                       form=form)
            elif freq == "weekly":
                sales = Transactions.query.filter(or_(Transactions.transaction_type == "Sale")).all()
                sales_df = pd.DataFrame(
                    [{'Date': trans.transaction_date, "Amount": trans.amount, "Count": trans.product} for trans in
                     sales])
                sales_df.Date = pd.to_datetime(sales_df.Date)
                sales_df.set_index('Date', inplace=True)
                sales_df = sales_df.resample('W').agg({"Amount": "sum", "Count": "count"})
                sales_df = sales_df.sort_index(ascending=False)

                refund = Transactions.query.filter(or_(Transactions.transaction_type == "Refund",
                                                       Transactions.transaction_type == "Chargeback")).all()
                refund_df = pd.DataFrame(
                    [{'Date': trans.transaction_date, "Amount": trans.amount, "Count": trans.product} for trans in
                     refund])
                refund_df.Date = pd.to_datetime(refund_df.Date)
                refund_df.set_index('Date', inplace=True)
                refund_df = refund_df.resample('W').agg({"Amount": "sum", "Count": "count"})
                refund_df = refund_df.sort_index(ascending=False)

                return render_template('dash/summary.html', sales=sales_df, refunds=refund_df, db="transactions",
                                       form=form)
        else:
            sales = Transactions.query.filter(or_(Transactions.transaction_type == "Sale")).all()
            sales_df = pd.DataFrame(
                [{'Date': trans.transaction_date, "Amount": trans.amount, "Count": trans.product} for trans in sales])
            sales_df.Date = pd.to_datetime(sales_df.Date)
            sales_df.set_index('Date', inplace=True)
            sales_df = sales_df.resample('MS').agg({"Amount": "sum", "Count": "count"})
            sales_df = sales_df.sort_index(ascending=False)

            refund = Transactions.query.filter(or_(Transactions.transaction_type == "Refund",
                                                   Transactions.transaction_type == "Chargeback")).all()
            refund_df = pd.DataFrame(
                [{'Date': trans.transaction_date, "Amount": trans.amount, "Count": trans.product} for trans in refund])
            refund_df.Date = pd.to_datetime(refund_df.Date)
            refund_df.set_index('Date', inplace=True)
            refund_df = refund_df.resample('MS').agg({"Amount": "sum", "Count": "count"})
            refund_df = refund_df.sort_index(ascending=False)

            return render_template('dash/summary.html', sales=sales_df, refunds=refund_df, db="transactions", form=form)

    except:
        return render_template('dash/summary.html', db="transactions", form=form)


@main_bp.route('/dash', methods=['GET', 'POST'])
@main_bp.route('/home', methods=['GET', 'POST'])
@main_bp.route('/', methods=['GET', 'POST'])
@login_required
def dash():
    form = DashForm()
    data = "sales"
    iframe = de(data)

    if form.validate_on_submit():
        data = form.dash.data
        iframe = de(data)

        return render_template('dash/dash.html', form=form, iframe=iframe, data=data)

    else:
        return render_template('dash/dash.html', form=form, iframe=iframe, data=data)


@main_bp.route('/webinar', methods=['GET', 'POST'])
@login_required
def webinar():
    page = request.args.get('page', 1, type=int)
    data_set = WebinarFunnelStarts.query.order_by(desc(WebinarFunnelStarts.date)).paginate(page=page, per_page=per_page)
    count = WebinarFunnelStarts.query.count()
    return render_template('tables/webinar.html', data_set=data_set, db="webinar", count=count)


@main_bp.route('/youtube', methods=['GET', 'POST'])
@login_required
def youtube():
    form = YoutubeForm()
    if form.validate_on_submit():
        if form.type.data == 'calls':
            page = request.args.get('page', 1, type=int)
            data_set = YoutubeCalls.query.order_by(desc(YoutubeCalls.week_end)).paginate(page=page, per_page=per_page)
            count = YoutubeCalls.query.count()
            return render_template('tables/youtube.html', data_set=data_set, db="Calls", count=count, form=form)

        elif form.type.data == 'webinar':
            page = request.args.get('page', 1, type=int)
            data_set = YoutubeWebinar.query.order_by(desc(YoutubeWebinar.week_end)).paginate(page=page,
                                                                                             per_page=per_page)
            count = YoutubeCalls.query.count()
            return render_template('tables/youtube.html', data_set=data_set, db="Webinar", count=count, form=form)

    else:
        page = request.args.get('page', 1, type=int)
        data_set = YoutubeCalls.query.order_by(desc(YoutubeCalls.week_end)).paginate(page=page, per_page=per_page)
        count = YoutubeCalls.query.count()
        return render_template('tables/youtube.html', data_set=data_set, db="Calls", count=count, form=form)


@main_bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()
    if form.is_submitted():
        csv_file = form.file.data
        table = form.database.data
        try:
            # Read the CSV file using pandas
            df = pd.read_csv(csv_file)
            # Insert or update data in the database
            um(table, df)
            db.session.commit()
            db.session.flush()
            flash('CSV data successfully inserted into the database!', 'success')

        except Exception as e:
            db.session.rollback()
            flash(f'Error inserting/updating data:{str(e)}', 'danger')

        return redirect(url_for('main.upload'))

    return render_template('upload.html', form=form)
