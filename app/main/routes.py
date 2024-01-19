from flask import render_template, flash, redirect, url_for, request
from sqlalchemy import or_, desc
from flask_login import login_required
import pandas as pd
from datetime import datetime


import traceback

from . import main_bp
from .forms import *
from .models import *

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
    data_set = Members.query.paginate(page=page, per_page=per_page)
    return render_template('tables/leads.html', data_set=data_set, db="leads")


@main_bp.route('/transactions', methods=['GET', 'POST'])
@login_required
def transactions():
    form = TransactionForm()
    if form.is_submitted():
        if form.type.data == 'all':
            page = request.args.get('page', 1, type=int)
            data_set = Transactions.query.paginate(page=page, per_page=per_page)
            count = Transactions.query.count()
            return render_template('tables/transactions.html', data_set=data_set, db="All Transactions", form=form, count=count)

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
        return render_template('tables/transactions.html', data_set=data_set, db="All Transactions", form=form, count=count)



@main_bp.route('/summary', methods=['GET', 'POST'])
@login_required
def summary():
    form = SumForm()
    if form.is_submitted():
        freq = form.freq.data
        if freq == "monthly":
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

            return render_template('dash/dash.html', sales=sales_df, refunds=refund_df, db="transactions", form=form)
        elif freq == "weekly":
            sales = Transactions.query.filter(or_(Transactions.transaction_type == "Sale")).all()
            sales_df = pd.DataFrame(
                [{'Date': trans.transaction_date, "Amount": trans.amount, "Count": trans.product} for trans in sales])
            sales_df.Date = pd.to_datetime(sales_df.Date)
            sales_df.set_index('Date', inplace=True)
            sales_df = sales_df.resample('W').agg({"Amount": "sum", "Count": "count"})
            sales_df = sales_df.sort_index(ascending=False)

            refund = Transactions.query.filter(or_(Transactions.transaction_type == "Refund",
                                                   Transactions.transaction_type == "Chargeback")).all()
            refund_df = pd.DataFrame(
                [{'Date': trans.transaction_date, "Amount": trans.amount, "Count": trans.product} for trans in refund])
            refund_df.Date = pd.to_datetime(refund_df.Date)
            refund_df.set_index('Date', inplace=True)
            refund_df = refund_df.resample('W').agg({"Amount": "sum", "Count": "count"})
            refund_df = refund_df.sort_index(ascending=False)

            return render_template('dash/dash.html', sales=sales_df, refunds=refund_df, db="transactions", form=form)
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


@main_bp.route('/dash', methods=['GET', 'POST'])
@main_bp.route('/home', methods=['GET', 'POST'])
@main_bp.route('/', methods=['GET', 'POST'])
def dash():
    form = DashForm()
    data = "sales"
    iframe = f"""
                    <iframe width="100%" height="850" 
                        src="https://lookerstudio.google.com/embed/reporting/c4ba13f0-14a9-4e7f-9f0e-a54058e41204/page/XM0mD"
                        frameborder="0" 
                        style="border:0" 
                        allowfullscreen 
                        andbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">
                    </iframe>
                """
    if form.validate_on_submit():
        data = form.dash.data

        if data == 'sales':
            iframe = """
                <iframe width="100%" height="850" 
                    src="https://lookerstudio.google.com/embed/reporting/c4ba13f0-14a9-4e7f-9f0e-a54058e41204/page/XM0mD"
                    frameborder="0" 
                    style="border:0" 
                    allowfullscreen 
                    andbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">
                </iframe>
            """
        elif data == 'webinar':
            iframe = """
                <iframe width="100%" height="850" 
                    src="https://lookerstudio.google.com/embed/reporting/c4ba13f0-14a9-4e7f-9f0e-a54058e41204/page/XM0mD"
                    frameborder="0" 
                    style="border:0" 
                    allowfullscreen 
                    andbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">
                </iframe>
            """
        elif data == 'youtube':
            iframe = """
                <iframe width="100%" height="850" 
                    src="https://lookerstudio.google.com/embed/reporting/c4ba13f0-14a9-4e7f-9f0e-a54058e41204/page/XM0mD"
                    frameborder="0" 
                    style="border:0" 
                    allowfullscreen 
                    andbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">
                </iframe>
            """
        return render_template('dash/dash.html', form=form, iframe=iframe, data=data)

    else:
        return render_template('dash/dash.html', form=form, iframe=iframe, data=data)



@main_bp.route('/webinar', methods=['GET', 'POST'])
@login_required
def webinar():
    page = request.args.get('page', 1, type=int)
    data_set = WebinarFunnelStarts.query.order_by(desc(WebinarFunnelStarts.date)).paginate(page=page, per_page=per_page)
    count = WebinarFunnelStarts.query.count()
    return render_template('tables/webinar.html', data_set=data_set, db="webinar",count=count)

@main_bp.route('/youtube', methods=['GET', 'POST'])
@login_required
def youtube():
    page = request.args.get('page', 1, type=int)
    data_set = YoutubeStats.query.order_by(desc(YoutubeStats.week_end)).paginate(page=page, per_page=per_page)
    count = YoutubeStats.query.count()
    return render_template('tables/youtube.html', data_set=data_set, db="Youtube",count=count)


@main_bp.route('/upload', methods=['GET', 'POST'])
@main_bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()
    if form.is_submitted():
        csv_file = form.file.data
        data = form.database.data
        try:
            # Read the CSV file using pandas
            df = pd.read_csv(csv_file)
            # Insert or update data in the database
            if data == "members":
                for index, row in df.iterrows():
                    # Try to load an existing member with the same email
                    existing_member = Members.query.filter_by(email=row['Email']).first()

                    if existing_member:
                        # Update existing member
                        Members.query.filter_by(id=existing_member.id).update({
                            "first_name": row['First Name'],
                            "last_name": row['Last Name'],
                            "program": row['Membership'],
                            "access": row['Active Membership Access']
                        })
                    else:
                        # Insert new member
                        member = Members(first_name=row['First Name'],
                                         last_name=row['Last Name'],
                                         email=row['Email'],
                                         program=row['Membership'],
                                         access=row['Active Membership Access'])
                        db.session.add(member)

            if data == "transactions":
                for index, row in df.iterrows():
                    # Try to load an existing transaction with the same transaction_id
                    existing_transaction = Transactions.query.filter_by(transaction_id=row['ID']).first()

                    if existing_transaction:
                        # Update existing transaction
                        Transactions.query.filter_by(id=existing_transaction.id).update({
                            "transaction_date": datetime.strptime(row['Date'], '%Y-%m-%d %H:%M:%S'),
                            "transaction_type": row["Transaction_Type"],
                            "product": row["Product"],
                            "buyer_name": row["Buyer_Name"],
                            "buyer_email": row["Buyer_Email"],
                            "buyer_username": row["Buyer_Username"],
                            "buyer_country": row["Buyer_Country"],
                            "buyer_state": row["Buyer_State"],
                            "amount": row["Amount (USD)"]
                        })
                    else:
                        # Insert new transaction
                        transaction = Transactions(
                            transaction_id=row['ID'],
                            transaction_date=datetime.strptime(row['Date'], '%Y-%m-%d %H:%M:%S'),
                            transaction_type=row["Transaction_Type"],
                            product=row["Product"],
                            buyer_name=row["Buyer_Name"],
                            buyer_email=row["Buyer_Email"],
                            buyer_username=row["Buyer_Username"],
                            buyer_country=row["Buyer_Country"],
                            amount=row["Amount (USD)"]
                        )
                        db.session.add(transaction)

            if data == "webinar":
                for index, row in df.iterrows():
                    # Try to load an existing transaction with the same transaction_id
                    existing_webinar = WebinarFunnelStarts.query.filter_by(date=row['Date']).first()

                    if existing_webinar:
                        # Update existing transaction
                        WebinarFunnelStarts.query.filter_by(id=existing_webinar.id).update({
                            "date": datetime.strptime(row['Date'], '%d/%m/%Y'),
                            "adspend": row["Adspend (USD)"],
                            "impressions": row["Impr"],
                            "clicks": row["Clicks"],
                            "leads": row["Leads"],
                            "sales": row["Sales"],
                        })
                    else:
                        # Insert new transaction
                        webinar_data = WebinarFunnelStarts(
                            date=datetime.strptime(row["Date"], '%d/%m/%Y'),
                            adspend=row["Adspend (USD)"],
                            impressions=row["Impr"],
                            clicks=row["Clicks"],
                            leads=row["Leads"],
                            sales=row["Sales"])
                        db.session.add(webinar_data)

            if data == "youtube":
                for index, row in df.iterrows():
                    # Try to load an existing transaction with the same transaction_id
                    existing_week = YoutubeStats.query.filter_by(week_end=row['Week Ending']).first()

                    if existing_week:
                        # Update existing transaction
                        YoutubeStats.query.filter_by(id=existing_week.id).update({
                            "week_end": datetime.strptime(row['Week Ending'], '%d/%m/%y'),
                            "impressions": row["impressions"],
                            "clicks": row["Clicks"],
                            "cost": row["Cost"],
                            "leads": row["Leads"],
                            "calls": row["Calls"],
                            "sales": row["Sales"],
                            "revenue": row["Revenue"],
                        })
                    else:
                        # Insert new transaction
                        youtube = YoutubeStats(
                            week_end=datetime.strptime(row['Week Ending'], '%d/%m/%y'),
                            impressions=row["Impressions"],
                            clicks=row["Clicks"],
                            cost=row["Cost"],
                            leads=row["Leads"],
                            calls=row["Calls"],
                            sales=row["Sales"],
                            revenue=row["Revenue"],
                        )
                        db.session.add(youtube)

            db.session.commit()
            db.session.flush()
            flash('CSV data successfully inserted into the database!', 'success')

        except Exception as e:
            db.session.rollback()
            flash(f'Error inserting/updating data:{str(e)}', 'danger')

        return redirect(url_for('main.upload'))

    return render_template('upload.html', form=form)
