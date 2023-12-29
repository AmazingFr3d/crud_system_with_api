from flask import Blueprint

main_bp = Blueprint("main", __name__, url_prefix='')

from . import routes
from . import forms
from . import models