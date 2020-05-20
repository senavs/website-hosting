from flask import Blueprint

from .views import cadastrar, listar, alterar

app_hospedagem = Blueprint('hospedagem', __name__,
                           url_prefix='/hospedagem')

app_hospedagem.add_url_rule('/listar', 'listar', listar, methods=['GET', 'POST'])
app_hospedagem.add_url_rule('/cadastrar', 'cadastrar', cadastrar, methods=['GET', 'POST'])
app_hospedagem.add_url_rule('/alterar', 'alterar', alterar, methods=['GET', 'POST'])
