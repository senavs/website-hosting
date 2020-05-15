import os

from flask import Blueprint

from .views import listar, alterar_disponibilizade, cadastrar, deletar
from ...configuration import BASE_DIR

# import your views route here

app_quarto = Blueprint('quarto', __name__,
                       url_prefix='/quarto',
                       static_folder='static',
                       static_url_path=os.path.join(BASE_DIR, 'project', 'frontend', 'static'),
                       template_folder=os.path.join(BASE_DIR, 'project', 'frontend', 'templates'))

# add your views route here
app_quarto.add_url_rule('/listar', 'listar', listar)
app_quarto.add_url_rule('/cadastrar', 'cadastrar', cadastrar, methods=['GET', 'POST'])
app_quarto.add_url_rule('/alterar-disponibilizade', 'alterar-disponibilizade', alterar_disponibilizade, methods=['GET', 'POST'])
app_quarto.add_url_rule('/deletar', 'deletar', deletar, methods=['GET', 'POST'])
