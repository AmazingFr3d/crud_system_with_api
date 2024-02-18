from datetime import datetime

from .models import *


def member_import(data):
    for index, row in data.iterrows():
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


def transaction_helper(data):
    for index, row in data.iterrows():
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


def webinar_helper(data):
    for index, row in data.iterrows():
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


def yt_call_helper(data):
    for index, row in data.iterrows():
        # Try to load an existing transaction with the same transaction_id
        existing_call = YoutubeCalls.query.filter_by(week_end=row['Week Ending']).first()

        if existing_call:
            # Update existing transaction
            YoutubeCalls.query.filter_by(id=existing_call.id).update({
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
            youtube_call = YoutubeCalls(
                week_end=datetime.strptime(row['Week Ending'], '%d/%m/%y'),
                impressions=row["Impressions"],
                clicks=row["Clicks"],
                cost=row["Cost"],
                leads=row["Leads"],
                calls=row["Calls"],
                sales=row["Sales"],
                revenue=row["Revenue"],
            )
            db.session.add(youtube_call)


def yt_webinar_helper(data):
    for index, row in data.iterrows():
        # Try to load an existing transaction with the same transaction_id
        existing_webinar = YoutubeWebinar.query.filter_by(week_end=row['Week Ending']).first()

        if existing_webinar:
            # Update existing transaction
            YoutubeCalls.query.filter_by(id=existing_webinar.id).update({
                "week_end": datetime.strptime(row['Week Ending'], '%d/%m/%y'),
                "impressions": row["impressions"],
                "clicks": row["Clicks"],
                "cost": row["Cost"],
                "leads": row["Leads"],
                "checkouts": row["Checkouts"],
                "sales": row["Sales"],
                "revenue": row["Revenue"],
            })
        else:
            # Insert new transaction
            youtube_webinar = YoutubeWebinar(
                week_end=datetime.strptime(row['Week Ending'], '%d/%m/%y'),
                impressions=row["Impressions"],
                clicks=row["Clicks"],
                cost=row["Cost"],
                leads=row["Leads"],
                checkouts=row["Checkouts"],
                sales=row["Sales"],
                revenue=row["Revenue"],
            )
            db.session.add(youtube_webinar)


def lead_helper(data):
    for index, row in data.iterrows():
        # Try to load an existing transaction with the same transaction_id
        existing_lead = Leads.query.filter_by(email=row['Email']).first()

        if existing_lead:
            # Update existing transaction
            Leads.query.filter_by(id=existing_lead.id).update({
                "fname": row['First Name'],
                "lname": row["Last Name"],
                "email": row["Email"],
                "phone": row["First Phone"],
                "industry": row["Industry"],
                "country": row["Country"],
                "state": row["State"],
                "stage": row["Stage"],
            })
        else:
            # Insert new transaction
            lead = Leads(
                fname=row['First Name'],
                lname=row["Last Name"],
                email=row["Email"],
                phone=row["First Phone"],
                industry=row["Industry"],
                country=row["Country"],
                state=row["State"],
                stage=row["Stage"],
            )
            db.session.add(lead)


def upload_map(table: str, data):
    tables = {
        "members": member_import(data),
        "transactions": transaction_helper(data),
        "webinar": webinar_helper(data),
        "youtube_call": yt_call_helper(data),
        "youtube_webinar": yt_webinar_helper(data),
        "leads": lead_helper(data),
    }
    tables.get(table)
