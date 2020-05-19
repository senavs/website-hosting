from flask import Blueprint

from .views import listar, cadastrar, pesquisar, alterar, deletar

app_funcionario = Blueprint('funcionario', __name__,
                            url_prefix='/funcionario')

app_funcionario.add_url_rule('/listar', 'listar', listar)
app_funcionario.add_url_rule('/cadastrar', 'cadastrar', cadastrar, methods=['GET', 'POST'])
app_funcionario.add_url_rule('/pesquisar', 'pesquisar', pesquisar, methods=['GET', 'POST'])
app_funcionario.add_url_rule('/alterar', 'alterar', alterar, methods=['GET', 'POST'])
app_funcionario.add_url_rule('/deletar', 'deletar', deletar, methods=['GET', 'POST'])
