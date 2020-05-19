from flask import Blueprint

from .views import listar, cadastrar, pesquisar, alterar, deletar

app_hospede = Blueprint('hospede', __name__,
                        url_prefix='/hospede')

app_hospede.add_url_rule('/listar', 'listar', listar)
app_hospede.add_url_rule('/cadastrar', 'cadastrar', cadastrar, methods=['GET', 'POST'])
app_hospede.add_url_rule('/pesquisar', 'pesquisar', pesquisar, methods=['GET', 'POST'])
app_hospede.add_url_rule('/alterar', 'alterar', alterar, methods=['GET', 'POST'])
app_hospede.add_url_rule('/deletar', 'deletar', deletar, methods=['GET', 'POST'])
