from sqlite3 import OperationalError, IntegrityError

from flask import request, make_response, render_template, url_for, abort, redirect, flash

from .models import TipoPagamentoModel
from ..main.models import DatabaseException
from ...configuration import DATABASE_URL


def listar():
    with TipoPagamentoModel(DATABASE_URL) as db:
        try:
            tipo_pagamento = db.select_all()
        except (DatabaseException, OperationalError, IntegrityError) as err:
            flash(str(err), 'danger')
            return render_template('tipo_pagamento-listar.html')
    return render_template('tipo_pagamento-listar.html', tipo_pagamento=tipo_pagamento)


def cadastrar():
    if request.method == 'POST':
        with TipoPagamentoModel(DATABASE_URL) as db:
            try:
                db.insert(request.form['NO_TIPO_PAGAMENTO'])
            except (DatabaseException, OperationalError, IntegrityError) as err:
                flash(str(err), 'danger')
                return redirect(url_for('tipo_pagamento.cadastrar'))
            else:
                db.commit()
                flash('Cadastrado com sucesso', 'success')
    return render_template('tipo_pagamento-cadastrar.html')


def deletar():
    with TipoPagamentoModel(DATABASE_URL) as db:
        if request.method == 'POST':
            try:
                db.delete(request.form['ID_TIPO_PAGAMENTO'])
            except (DatabaseException, OperationalError, IntegrityError) as err:
                flash(str(err), 'danger')
                return redirect(url_for('tipo_pagamento.deletar'))
            else:
                db.commit()
                flash('Deletado com sucesso', 'success')
        tipo_pagamento = db.select_all()
    return render_template('tipo_pagamento-deletar.html', tipo_pagamento=tipo_pagamento)
