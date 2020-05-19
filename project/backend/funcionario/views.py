from sqlite3 import OperationalError, IntegrityError

from flask import request, render_template, url_for, redirect, flash, session

from .models import Funcionario, FuncionarioEnderecoView
from ..main.models import DatabaseException
from ...configuration import DATABASE_URL


def listar():
    with FuncionarioEnderecoView(DATABASE_URL) as db:
        funcionarios = db.select_all()
    return render_template('funcionario-listar.html', funcionarios=funcionarios)


def cadastrar():
    if request.method == 'POST':
        with Funcionario(DATABASE_URL) as db:
            try:
                id_endereco = db.insert_endereco(request.form['NU_CEP'], request.form['NO_ENDERECO'],
                                                 request.form['NO_COMPLEMENTO'], request.form['NU_NUMERO'])
                db.insert(request.form['NU_CPF'], request.form['NO_FUNCIONARIO'],
                          request.form['NU_TELEFONE'], request.form['NO_EMAIL'], id_endereco)
            except (DatabaseException, OperationalError, IntegrityError) as err:
                flash(str(err), 'danger')
                db.rollback()
                return redirect(url_for('funcionario.cadastrar'))
            else:
                db.commit()
                flash('Cadastrado com sucesso', 'success')
    return render_template('funcionario-cadastrar.html')


def pesquisar():
    with FuncionarioEnderecoView(DATABASE_URL) as db:
        funcionarios = db.select_all()
        if request.method == 'POST':
            funcionario = db.select_all_by(id_funcionario=request.form['ID_FUNCIONARIO'])
            session['funcionario'] = funcionario
            return redirect(url_for('funcionario.alterar'))
    return render_template('funcionario-pesquisar.html', funcionarios=funcionarios)


def alterar():
    try:
        funcionario = session['funcionario'][0]
    except KeyError:
        return redirect(url_for('funcionario.pesquisar'))

    if request.method == 'POST':
        with Funcionario(DATABASE_URL) as db:
            try:
                db.update(funcionario['ID_FUNCIONARIO'], request.form['NU_TELEFONE'], request.form['NO_EMAIL'])
                db.update_endereco(funcionario['ID_ENDERECO'], request.form['NU_CEP'], request.form['NO_ENDERECO'],
                                   request.form['NO_COMPLEMENTO'], request.form['NU_NUMERO'])
            except (DatabaseException, OperationalError, IntegrityError) as err:
                flash(str(err), 'danger')
                db.rollback()
                return redirect(url_for('funcionario.pesquisar'))
            else:
                db.commit()
                flash('Alterado com sucesso', 'success')
                return redirect(url_for('funcionario.pesquisar'))

    return render_template('funcionario-alterar.html', funcionario=funcionario)


def deletar():
    if request.method == 'POST':
        with Funcionario(DATABASE_URL) as db:
            ids = request.form['ID_FUNCIONARIO-ID_ENDERECO'].split('-')
            try:
                db.delete(ids[0])
                db.delete_endereco(ids[1])
            except (DatabaseException, OperationalError, IntegrityError) as err:
                flash(str(err), 'danger')
                db.rollback()
                return redirect(url_for('funcionario.deletar'))
            else:
                db.commit()
                flash('Deletado com sucesso', 'success')

    with FuncionarioEnderecoView(DATABASE_URL) as db:
        funcionarios = db.select_all()

    return render_template('funcionario-deletar.html', funcionarios=funcionarios)
