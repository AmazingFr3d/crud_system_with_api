from .. import db

class WebinarFunnelStarts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    adspend = db.Column(db.Float)
    impressions = db.Column(db.Integer)
    clicks = db.Column(db.Integer)
    leads = db.Column(db.Integer)
    sales = db.Column(db.Integer)

    def __init__(self, date, adspend, impressions, clicks, leads, sales):
        self.date = date
        self.adspend = adspend
        self.impressions = impressions
        self.clicks = clicks
        self.leads = leads
        self.sales = sales


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.String(120))
    transaction_date = db.Column(db.Date)
    transaction_type = db.Column(db.String(20))
    product = db.Column(db.Integer)
    buyer_email = db.Column(db.String(120))
    buyer_name = db.Column(db.String(120))
    buyer_username = db.Column(db.String(120))
    buyer_state = db.Column(db.String(120))
    buyer_country = db.Column(db.String(120))
    amount = db.Column(db.Float)

    def __init__(self, transaction_id, transaction_date, transaction_type, product, buyer_email, buyer_name,
                 buyer_username, buyer_country, amount):
        self.transaction_id = transaction_id
        self.transaction_date = transaction_date
        self.transaction_type = transaction_type
        self.product = product
        self.buyer_email = buyer_email
        self.buyer_name = buyer_name
        self.buyer_username = buyer_username
        self.buyer_country = buyer_country
        self.amount = amount


class Leads(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    email = db.Column(db.String(120))
    fname = db.Column(db.String(120))
    lname = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    industry = db.Column(db.String(120))
    country = db.Column(db.String(120))
    state = db.Column(db.String(120))
    stage = db.Column(db.String(120))

    def __init__(self, email, fname, lname, phone, industry, country, state, stage):
        self.email = email
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.industry = industry
        self.country = country
        self.state = state
        self.stage = stage


class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50),)
    last_name = db.Column(db.String(50),)
    email = db.Column(db.String(120))
    program = db.Column(db.String(120))
    access = db.Column(db.String(120))

    def __init__(self, first_name, last_name, email, program, access):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.program = program
        self.access = access


class YoutubeCalls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    week_end = db.Column(db.Date)
    impressions = db.Column(db.Float)
    clicks = db.Column(db.Float)
    cost = db.Column(db.Float)
    leads = db.Column(db.Float)
    calls = db.Column(db.Float)
    sales = db.Column(db.Float)
    revenue = db.Column(db.Float)

    def __init__(self, week_end, impressions, clicks, cost, leads, calls, sales, revenue):
        self.week_end = week_end
        self.impressions = impressions
        self.clicks = clicks
        self.cost = cost
        self.leads = leads
        self.calls = calls
        self.sales = sales
        self.revenue = revenue


class YoutubeWebinar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    week_end = db.Column(db.Date)
    impressions = db.Column(db.Float)
    clicks = db.Column(db.Float)
    cost = db.Column(db.Float)
    leads = db.Column(db.Float)
    checkouts = db.Column(db.Float)
    sales = db.Column(db.Float)
    revenue = db.Column(db.Float)

    def __init__(self, week_end, impressions, clicks, cost, leads, checkouts, sales, revenue):
        self.week_end = week_end
        self.impressions = impressions
        self.clicks = clicks
        self.cost = cost
        self.leads = leads
        self.checkouts = checkouts
        self.sales = sales
        self.revenue = revenue
