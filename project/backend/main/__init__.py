import os

from flask import Blueprint

from ...configuration import BASE_DIR
from .views import home
from .error import erro_404

# import your views route here

app_main = Blueprint('main', __name__,
                     url_prefix='/',
                     static_folder='static',
                     static_url_path=os.path.join(BASE_DIR, 'project', 'frontend', 'static'),
                     template_folder=os.path.join(BASE_DIR, 'project', 'frontend', 'templates'))

# add your views route here
app_main.add_url_rule('/', 'home', home)

# add your error handlers here
app_main.app_errorhandler(404)(erro_404)
