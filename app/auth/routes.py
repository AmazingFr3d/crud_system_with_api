from flask import render_template, redirect, url_for, flash, session, request
from flask_login import login_user, logout_user, current_user, login_required
from .models import User
from . import auth_bp
from .. import db
from .functions import send_password_reset_email
from .forms import RegisterForm, LoginForm, PassResetForm
import datetime


@auth_bp.route('/')
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('main.members'))

    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email=form.email.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(user=attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.name}', category='success')
            return redirect(url_for('main.dash'))
        else:
            flash('Login unsuccessful. Please check email and password', category='danger')

    return render_template('auth/login.html', form=form)


@auth_bp.route('/register', methods=['GET', 'POST'])
# @login_required
def register():
    # if current_user.role == 'admin':
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(name=form.name.data,
                              email=form.email.data,
                              password=form.confirm.data,
                              role=form.role.data)
        db.session.add(user_to_create)
        db.session.commit()
        flash(f'User created!', category='success')
        return redirect(url_for('auth.login'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'{err_msg}', category='warning')
    return render_template('auth/register.html', form=form)
    # else:
    #     return redirect(url_for('main.summary'))


@auth_bp.route('/users')
@login_required
def users():
    if current_user.role == 'admin':
        sys_users = User.query.all()
        return render_template('auth/users.html', users=sys_users)
    else:
        return redirect(url_for('main.summary'))


@auth_bp.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for('auth.login'))


@auth_bp.route('/delete_user/<int:user_id>', methods=["POST"])
@login_required
def delete_user(user_id):
    if current_user.role == 'admin':
        if current_user.id != user_id:
            user_to_delete = User.query.get(user_id)
            db.session.delete(user_to_delete)
            db.session.commit()
            flash("User deleted", category='info')
            return redirect(url_for('auth.users'))
        else:
            flash("You cannot delete yourself!", category='warning')
            return redirect(url_for('auth.users'))
    else:
        return redirect(url_for('main.summary'))


@auth_bp.route('/send_pass_reset/<email>', methods=['GET', 'POST'])
def send_pass_reset(email):
    if request.method == 'POST':
        user = User.query.filter_by(email=email).first()
        if user:
            user.generate_reset_token()
            db.session.commit()

            send_password_reset_email(user.email, user.reset_token)

            flash(f'Password reset link sent to your {user.email}.', 'info')
            return redirect(url_for('auth.users'))
        flash('No user found with that email address.', 'danger')


@auth_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    form = PassResetForm()

    if form.validate_on_submit():
        user = User.query.filter_by(reset_token=token).first()

        if user and user.reset_token_expiration > datetime.datetime.utcnow():
            if request.method == 'POST':
                User.query.filter_by(reset_token=user.reset_token).update(password=request.form.get('new_password'),
                                                                          reset_token=None,
                                                                          reset_token_expiration=None)
                db.session.commit()

                flash('Password reset successful. You can now log in with your new password.', 'success')
                return redirect(url_for('auth.login'))

            return render_template('auth/pass_reset.html', token=token, form=form)

        flash('Password reset link is invalid or has expired.', 'danger')
        return redirect(url_for('auth.login'))
