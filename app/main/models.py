from .. import db


class WebinarFunnelStarts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    adspend = db.Column(db.Float)
    impressions = db.Column(db.Integer)
    cpm = db.Column(db.Float)
    clicks = db.Column(db.Integer)
    ctr = db.Column(db.Float)
    cpc = db.Column(db.Float)
    leads = db.Column(db.Integer)
    lp_cvr = db.Column(db.Float)
    cpl = db.Column(db.Float)
    wa = db.Column(db.Float)
    war = db.Column(db.Float)
    cpwar = db.Column(db.Float)
    sales = db.Column(db.Integer)
    cpa = db.Column(db.Float)


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_date = db.Column(db.Date)
    transaction_type = db.Column(db.String(20))
    lead_id = db.Column(db.Integer)
    email = db.Column(db.String(120))
    name = db.Column(db.String(120))
    offer_purchased = db.Column(db.String(120))
    amount_paid = db.Column(db.Float)
    balance_due = db.Column(db.Float)
    billing_location = db.Column(db.String(120))
    discount = db.Column(db.Float)
    discount_code = db.Column(db.String(120))


class Leads(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.Integer)
    email = db.Column(db.String(120))
    name = db.Column(db.String(120))
    job_description = db.Column(db.String(120))


class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer)
    email = db.Column(db.String(120))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    program = db.Column(db.String(120))
    access = db.Column(db.String(120))
