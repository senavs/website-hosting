from flask import Blueprint

from .views import home

# import your views route here
app_main = Blueprint('main', __name__,
                     url_prefix='/')

# add your views route here
app_main.add_url_rule('/', 'home', home)

# add your error handlers here
