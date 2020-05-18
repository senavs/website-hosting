from sqlite3 import OperationalError, IntegrityError

from flask import request, make_response, render_template, url_for, abort, redirect, flash

from .models import TipoQuartoModel
from ..main.models import DatabaseException
from ...configuration import DATABASE_URL


def listar():
    with TipoQuartoModel(DATABASE_URL) as db:
        try:
            tipo_quarto = db.select_all()
        except (DatabaseException, OperationalError, IntegrityError) as err:
            flash(str(err), 'danger')
            return render_template('tipo_quarto-listar.html')
    return render_template('tipo_quarto-listar.html', tipo_quarto=tipo_quarto)


def cadastrar():
    if request.method == 'POST':
        with TipoQuartoModel(DATABASE_URL) as db:
            try:
                db.insert(request.form['NO_TIPO_QUARTO'], request.form['VL_DIARIA'])
            except (DatabaseException, OperationalError, IntegrityError) as err:
                flash(str(err), 'danger')
                db.rollback()
                return redirect(url_for('tipo_quarto.cadastrar'))
            else:
                db.commit()
                flash('Cadastrado com sucesso', 'success')
    return render_template('tipo_quarto-cadastrar.html')


def alterar():
    with TipoQuartoModel(DATABASE_URL) as db:
        tipo_quarto = db.select_all()
        if request.method == 'POST':
            try:
                db.update(request.form['ID_TIPO_QUARTO'], request.form['VL_DIARIA'])
            except (DatabaseException, OperationalError, IntegrityError) as err:
                flash(str(err), 'danger')
                db.rollback()
                return redirect(url_for('tipo_quarto.alterar'))
            else:
                db.commit()
                flash('Alterado com sucesso', 'success')
    return render_template('tipo_quarto-alterar.html', tipo_quarto=tipo_quarto)


def deletar():
    with TipoQuartoModel(DATABASE_URL) as db:
        if request.method == 'POST':
            try:
                db.delete(request.form['ID_TIPO_QUARTO'])
            except (DatabaseException, OperationalError, IntegrityError) as err:
                flash(str(err), 'danger')
                db.rollback()
                return redirect(url_for('tipo_quarto.deletar'))
            else:
                db.commit()
                flash('Deletado com sucesso', 'success')
        tipo_quarto = db.select_all()
    return render_template('tipo_quarto-deletar.html', tipo_quarto=tipo_quarto)
