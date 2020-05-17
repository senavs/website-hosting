from flask import Blueprint

from .views import listar, cadastrar, deletar

# import your views route here
app_tipo_pagamento = Blueprint('tipo_pagamento', __name__,
                               url_prefix='/tipo_pagamento')

# add your views route here
app_tipo_pagamento.add_url_rule('/listar', 'listar', listar)
app_tipo_pagamento.add_url_rule('/cadastrar', 'cadastrar', cadastrar, methods=['GET', 'POST'])
app_tipo_pagamento.add_url_rule('/deletar', 'deletar', deletar, methods=['GET', 'POST'])

# add your error handlers here
