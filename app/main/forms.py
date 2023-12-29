from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError


class DbSelect(FlaskForm):
    database = SelectField('role', validators=[DataRequired()], choices=[('leads', 'Leads'),
                                                                         ('transactions', 'Transactions'),
                                                                         ('members', 'Members'),
                                                                         ('refunds', 'Refunds'),
                                                                         ('webinar_funnel', 'Webinar Funnel')])
    submit = SubmitField('Load Data')
