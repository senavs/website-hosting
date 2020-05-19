from sqlite3 import OperationalError, IntegrityError

from flask import request, render_template, url_for, redirect, flash, session

from .models import Hospede, HospedeEnderecoView
from ..main.models import DatabaseException
from ...configuration import DATABASE_URL


def listar():
    with HospedeEnderecoView(DATABASE_URL) as db:
        hospedes = db.select_all()
    return render_template('hospede-listar.html', hospedes=hospedes)


def cadastrar():
    if request.method == 'POST':
        with Hospede(DATABASE_URL) as db:
            try:
                id_endereco = db.insert_endereco(request.form['NU_CEP'], request.form['NO_ENDERECO'],
                                                 request.form['NO_COMPLEMENTO'], request.form['NU_NUMERO'])
                db.insert(request.form['NU_CPF'], request.form['NO_HOSPEDE'],
                          request.form['NU_TELEFONE'], request.form['NO_EMAIL'], id_endereco)
            except (DatabaseException, OperationalError, IntegrityError) as err:
                flash(str(err), 'danger')
                db.rollback()
                return redirect(url_for('hospede.cadastrar'))
            else:
                db.commit()
                flash('Cadastrado com sucesso', 'success')
    return render_template('hospede-cadastrar.html')


def pesquisar():
    with HospedeEnderecoView(DATABASE_URL) as db:
        hospedes = db.select_all()
        if request.method == 'POST':
            hospede = db.select_all_by(id_hospede=request.form['ID_HOSPEDE'])
            session['hospede'] = hospede
            return redirect(url_for('hospede.alterar'))
    return render_template('hospede-pesquisar.html', hospedes=hospedes)


def alterar():
    try:
        hospede = session['hospede'][0]
    except KeyError:
        return redirect(url_for('hospede.pesquisar'))

    if request.method == 'POST':
        with Hospede(DATABASE_URL) as db:
            try:
                db.update(hospede['ID_HOSPEDE'], request.form['NU_TELEFONE'], request.form['NO_EMAIL'])
                db.update_endereco(hospede['ID_ENDERECO'], request.form['NU_CEP'], request.form['NO_ENDERECO'],
                                   request.form['NO_COMPLEMENTO'], request.form['NU_NUMERO'])
            except (DatabaseException, OperationalError, IntegrityError) as err:
                flash(str(err), 'danger')
                db.rollback()
                return redirect(url_for('hospede.pesquisar'))
            else:
                db.commit()
                flash('Alterado com sucesso', 'success')
                return redirect(url_for('hospede.pesquisar'))

    return render_template('hospede-alterar.html', hospede=hospede)


def deletar():
    if request.method == 'POST':
        with Hospede(DATABASE_URL) as db:
            ids = request.form['ID_HOSPEDE-ID_ENDERECO'].split('-')
            try:
                db.delete(ids[0])
                db.delete_endereco(ids[1])
            except (DatabaseException, OperationalError, IntegrityError) as err:
                flash(str(err), 'danger')
                db.rollback()
                return redirect(url_for('hospede.deletar'))
            else:
                db.commit()
                flash('Deletado com sucesso', 'success')

    with HospedeEnderecoView(DATABASE_URL) as db:
        hospedes = db.select_all()

    return render_template('hospede-deletar.html', hospedes=hospedes)
