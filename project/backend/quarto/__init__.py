from flask import Blueprint

from .views import listar, cadastrar, deletar

app_quarto = Blueprint('quarto', __name__,
                       url_prefix='/quarto')

app_quarto.add_url_rule('/listar', 'listar', listar)
app_quarto.add_url_rule('/cadastrar', 'cadastrar', cadastrar, methods=['GET', 'POST'])
app_quarto.add_url_rule('/deletar', 'deletar', deletar, methods=['GET', 'POST'])
