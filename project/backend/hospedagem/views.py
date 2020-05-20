from datetime import datetime
from sqlite3 import OperationalError, IntegrityError

from flask import request, render_template, url_for, redirect, flash, session

from .models import HospedagemModel, HospedeDisponivelHospedagem, HospedagemDetalhadaView
from ..main.models import DatabaseException
from ..funcionario.models import Funcionario
from ..quarto.models import QuartoDisponivelView
from ..tipo_pagamento.views import TipoPagamentoModel
from ...configuration import DATABASE_URL


def pesquisar():
    with HospedagemDetalhadaView(DATABASE_URL) as db:
        hospedagens = db.select_all()
        hospedagem = None

    if request.method == 'POST':
        with HospedagemDetalhadaView(DATABASE_URL) as db:
            hospedagem = db.select_all_by(id_hospedagem=request.form['ID_HOSPEDAGEM'])[0]

    return render_template('hospedagem-pesquisar.html', hospedagens=hospedagens, hospedagem=hospedagem)


def cadastrar():
    data_hoje = datetime.now().strftime('%d/%m/%Y')
    if request.method == 'POST':
        with HospedagemModel(DATABASE_URL) as db:
            try:
                db.insert(request.form['ID_FUNCIONARIO'], request.form['ID_QUARTO'], request.form['ID_TIPO_PAGAMENTO'], request.form['ID_HOSPEDE_TITULAR'],
                          request.form['ID_HOSPEDE_ACOMPANHANTE_1'], request.form['ID_HOSPEDE_ACOMPANHANTE_2'], request.form['ID_HOSPEDE_ACOMPANHANTE_3'],
                          request.form['DT_ENTRADA'], request.form['NU_NOITE'])
            except (DatabaseException, OperationalError, IntegrityError) as err:
                flash(str(err), 'danger')
                db.rollback()
                return redirect(url_for('hospedagem.cadastrar'))
            else:
                db.commit()
                flash('Cadastrado com sucesso', 'success')

    with Funcionario(DATABASE_URL) as db:
        funcionarios = db.select_all()

    with QuartoDisponivelView(DATABASE_URL) as db:
        quartos = db.select_all()

    with TipoPagamentoModel(DATABASE_URL) as db:
        tipo_pagamento = db.select_all()

    with HospedeDisponivelHospedagem(DATABASE_URL) as db:
        hospedes = db.select_all()

    context = {
        'funcionarios': funcionarios,
        'quartos': quartos,
        'tipo_pagamento': tipo_pagamento,
        'hospedes': hospedes,
        'data_hoje': data_hoje
    }
    return render_template('hospedagem-cadastrar.html', **context)


def alterar():
    with HospedagemModel(DATABASE_URL) as db:
        hospedagens = db.select_all()

        if request.method == 'POST':
            try:
                db.update(request.form['ID_HOSPEDAGEM'], request.form['IN_ATIVO'])
            except (DatabaseException, OperationalError, IntegrityError) as err:
                flash(str(err), 'danger')
                db.rollback()
                return redirect(url_for('hospedagem.alterar'))
            else:
                db.commit()
                flash('Alterado com sucesso', 'success')

    return render_template('hospedagem-alterar.html', hospedagens=hospedagens)
