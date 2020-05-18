from flask import Blueprint

from .views import listar, cadastrar, alterar, deletar


app_tipo_quarto = Blueprint('tipo_quarto', __name__,
                            url_prefix='/tipo_quarto')

# add your views route here
app_tipo_quarto.add_url_rule('/listar', 'listar', listar)
app_tipo_quarto.add_url_rule('/cadastrar', 'cadastrar', cadastrar, methods=['GET', 'POST'])
app_tipo_quarto.add_url_rule('/alterar', 'alterar', alterar, methods=['GET', 'POST'])
app_tipo_quarto.add_url_rule('/deletar', 'deletar', deletar, methods=['GET', 'POST'])

# add your error handlers here
