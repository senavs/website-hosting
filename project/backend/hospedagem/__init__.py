from flask import Blueprint

from .views import cadastrar, pesquisar, alterar

app_hospedagem = Blueprint('hospedagem', __name__,
                           url_prefix='/hospedagem')

app_hospedagem.add_url_rule('/pesquisar', 'pesquisar', pesquisar, methods=['GET', 'POST'])
app_hospedagem.add_url_rule('/cadastrar', 'cadastrar', cadastrar, methods=['GET', 'POST'])
app_hospedagem.add_url_rule('/alterar', 'alterar', alterar, methods=['GET', 'POST'])
