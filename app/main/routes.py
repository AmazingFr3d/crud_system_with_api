from flask import render_template, flash, redirect, url_for
from . import main_bp
from .forms import DbSelect
from .models import *


@main_bp.route('/', methods=['GET', 'POST'])
@main_bp.route('/index', methods=['GET', 'POST'])
def dashboard():
    form = DbSelect()
    data_set = Leads.query.all()
    if form.is_submitted():
        data = form.database.data
        flash(f'Success! {data}', category='success')
        if data == "leads":
            data_set = Leads.query.all()
            return render_template("index.html",data_set=data_set, form=form, db=data)

        elif data == "transactions":
            data_set = Transactions.query.all()
            return render_template("index.html",data_set=data_set, form=form, db=data)

        elif data == "members":
            data_set = Members.query.all()
            return render_template("index.html",data_set=data_set, form=form, db=data)

        elif data == "refunds":
            data_set = Transactions.query.filter_by(transaction_type="refund").all()
            return render_template("index.html",data_set=data_set, form=form, db=data)

        elif data == "webinar_funnel":
            data_set = WebinarFunnelStarts.query.all()
            return render_template("index.html",data_set=data_set, form=form, db=data)

    return render_template('index.html', data_set=data_set, form=form, db="Leads")
