from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError


class DbSelect(FlaskForm):
    database = SelectField('role', validators=[DataRequired()], choices=[('leads', 'Leads'),
                                                                         ('transactions', 'Transactions'),
                                                                         ('members', 'Members'),
                                                                         ('refunds', 'Refunds'),
                                                                         ('webinar_funnel', 'Webinar Funnel')])
    submit = SubmitField('Load Data')


class UploadForm(FlaskForm):
    file = FileField('CSV File', validators=[FileRequired(), FileAllowed(['csv'], 'CSV Files only')])
    database = SelectField('role', validators=[DataRequired()], choices=[
        ('leads', 'Leads'), ('transactions', 'Transactions'), ('members', 'Members'), ('refunds', 'Refunds')])
    submit = SubmitField('Upload')
