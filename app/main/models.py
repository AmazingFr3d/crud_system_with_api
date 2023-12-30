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

    def __init__(self, date, adspend, impressions, cpm, clicks, ctr, cpc, leads, lp_cvr, cpl, wa, war, cpwar, sales, cpa):
        self.date = date
        self.adspend = adspend
        self.impressions = impressions
        self.cpm = cpm
        self.clicks = clicks
        self.ctr = ctr
        self.cpc = cpc
        self.leads = leads
        self.lp_cvr = lp_cvr
        self.cpl = cpl
        self.wa = wa
        self.war = war
        self.cpwar = cpwar
        self.sales = sales
        self.cpa = cpa


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

    def __init__(self, transaction_date, transaction_type, lead_id, email, name, offer_purchased, amount_paid
                  , balance_due, billing_location, discount, discount_code):
        self.transaction_date = transaction_date
        self.transaction_type = transaction_type
        self.lead_id = lead_id
        self.email = email
        self.name = name
        self.offer_purchased = offer_purchased
        self.amount_paid = amount_paid
        self.balance_due = balance_due
        self.billing_location = billing_location
        self.discount = discount
        self.discount_code = discount_code



class Leads(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.Integer)
    email = db.Column(db.String(120))
    name = db.Column(db.String(120))
    job_description = db.Column(db.String(120))

    def __init__(self, lead_id, email, name, job_description):
        self.lead_id = lead_id
        self.email = email
        self.name = name
        self.job_description = job_description


class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120))
    program = db.Column(db.String(120))
    access = db.Column(db.String(120))

    def __init__(self, first_name, last_name, email, program, access):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.program = program
        self.access = access
