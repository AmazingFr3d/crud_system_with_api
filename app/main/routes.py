from flask import render_template, flash, redirect, url_for, request
from sqlalchemy import or_
import pandas as pd
from datetime import datetime

from . import main_bp
from .forms import *
from .models import *

per_page = 50

@main_bp.route('/members', methods=['GET', 'POST'])
def members():
    page = request.args.get('page', 1, type=int)
    data_set = Members.query.paginate(page=page, per_page=per_page)
    return render_template('tables/members.html', data_set=data_set, db="members")


@main_bp.route('/leads', methods=['GET', 'POST'])
def leads():
    page = request.args.get('page', 1, type=int)
    data_set = Members.query.paginate(page=page, per_page=per_page)
    return render_template('tables/leads.html', data_set=data_set, db="leads")


@main_bp.route('/transactions', methods=['GET', 'POST'])
def transactions():
    page = request.args.get('page', 1, type=int)
    data_set = Members.query.paginate(page=page, per_page=per_page)
    return render_template('tables/transactions.html', data_set=data_set, db="transactions")


@main_bp.route('/refunds', methods=['GET', 'POST'])
def refunds():
    page = request.args.get('page', 1, type=int)

    data_set = Transactions.query.filter(or_(Transactions.transaction_type == "Refund",
                                             Transactions.transaction_type == "Chargeback")).paginate(page=page,
                                                                                                      per_page=per_page)

    return render_template('tables/transactions.html', data_set=data_set, db="refunds")


@main_bp.route('/webinar', methods=['GET', 'POST'])
def webinar():
    page = request.args.get('page', 1, type=int)
    data_set = Members.query.paginate(page=page, per_page=per_page)
    return render_template('tables/webinar.html', data_set=data_set, db="webinar")


@main_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.is_submitted():
        csv_file = form.file.data
        data = form.database.data
        li = []
        try:
            # Read the CSV file using pandas
            df = pd.read_csv(csv_file)
            # Insert data into the database
            if data == "members":
                for index, row in df.iterrows():

                    member = Members(first_name=row['First Name'],
                                     last_name=row['Last Name'],
                                     email=row['Email'],
                                     program=row['Membership'],
                                     access=row['Active Membership Access'])
                    db.session.add(member)

            if data == "transactions":
                print(len(df))
                for index, row in df.iterrows():
                    member = Transactions(transaction_id=row['ID'],
                                          transaction_date=datetime.strptime(row['Date'], '%Y-%m-%d %H:%M:%S'),
                                          transaction_type=row["Transaction_Type"],
                                          product=row["Product"],
                                          buyer_name=row["Buyer_Name"],
                                          buyer_email=row["Buyer_Email"],
                                          buyer_username=row["Buyer_Username"],
                                          buyer_country=row["Buyer_Country"],
                                          amount=row["Amount (USD)"])
                    db.session.add(member)

            db.session.commit()
            db.session.reset()

            flash('CSV data successfully inserted into the database!', 'success')

        except Exception as e:
            db.session.rollback()
            db.session.reset()
            flash(f'Error inserting data: {str(e)}', 'danger')

        return redirect(url_for('main.upload'))

    return render_template('upload.html', form=form)
