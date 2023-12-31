from flask import render_template, redirect, url_for, flash, session
from flask_login import login_user, logout_user, current_user, login_required
from .models import User
from . import auth_bp
from .. import db
from .forms import RegisterForm, LoginForm


@auth_bp.route('/')
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email=form.email.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(user=attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.buyer_name}', category='success')
            return redirect(url_for('main.home'))
        else:
            flash('Login unsuccessful. Please check email and password', category='danger')

    return render_template('auth/login.html', form=form)


@auth_bp.route('/register', methods=['GET', 'POST'])
# @login_required
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(name=form.name.data,
                              email=form.email.data,
                              password=form.confirm.data,
                              active="True",
                              role=form.role.data)
        db.session.add(user_to_create)
        db.session.commit()
        flash(f'User created!', category='success')
        return redirect(url_for('auth.user'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'{err_msg}', category='warning')
    return render_template('auth/register.html', form=form)


@auth_bp.route('/users')
# @login_required
def users():
    sys_users = User.query.all()
    return render_template('auth/users.html', users=sys_users)


@auth_bp.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for('auth.login'))


@auth_bp.route('/delete_user/<user_id>', methods=["POST"])
@login_required
def delete_user(user_id):
    user_to_delete = User.query.get(user_id)
    db.session.delete(user_to_delete)
    db.session.commit()
    flash("User deleted", category='info')
    return redirect(url_for('auth.users'))
