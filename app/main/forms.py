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
    database = SelectField('Table', validators=[DataRequired()], choices=[
        ('leads', 'Leads'),
        ('transactions', 'Transactions'),
        ('members', 'Members'),
        ('webinar', 'Webinar'),
        ('youtube_call', 'Youtube Calls'),
        ('youtube_webinar', 'Youtube Webinar')])
    submit = SubmitField('Upload')


class SumForm(FlaskForm):
    freq = SelectField('Time Frame', validators=[DataRequired()], choices=[
        ('monthly', 'Monthly'), ('weekly', 'Weekly')])
    submit = SubmitField('Switch')


class DashForm(FlaskForm):
    dash = SelectField('dash', validators=[DataRequired()], choices=[
        ('sales', 'Sales'), ('webinar', 'Webinar'), ('youtube', 'Youtube')])
    submit = SubmitField('Switch')


class TransactionForm(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()], choices=[
        ('sales', 'Sales'), ('refunds', 'Refunds'), ('all', 'All')])
    submit = SubmitField('Switch')


class YoutubeForm(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()], choices=[
        ('calls', 'Calls'), ('webinar', 'Webinar')])
    submit = SubmitField('Switch')
