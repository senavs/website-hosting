from sqlite3 import OperationalError, IntegrityError

from flask import request, render_template, url_for, redirect, flash

from .models import QuartoModel, QuartoTipoQuartView
from ..main.models import DatabaseException
from ..tipo_quarto.models import TipoQuartoModel
from ...configuration import DATABASE_URL


def listar():
    with QuartoTipoQuartView(DATABASE_URL) as db:
        try:
            quarto_tipo_quarto = db.select_all()
        except (DatabaseException, OperationalError, IntegrityError) as err:
            flash(str(err), 'danger')
            return render_template('quarto-listar.html')
    return render_template('quarto-listar.html', quarto_tipo_quarto=quarto_tipo_quarto)


def cadastrar():
    with TipoQuartoModel(DATABASE_URL) as db:
        tipo_quarto = db.select_all()

    if request.method == 'POST':
        with QuartoModel(DATABASE_URL) as db:
            try:
                db.insert(request.form['NU_QUARTO'], request.form['IN_DISPONIVEL'], request.form['ID_TIPO_QUARTO'])
            except (DatabaseException, OperationalError, IntegrityError) as err:
                flash(str(err), 'danger')
                return redirect(url_for('quarto.cadastrar'))
            else:
                db.commit()
                flash('Cadastrado com sucesso', 'success')
    return render_template('quarto-cadastrar.html', tipo_quarto=tipo_quarto)


def alterar():
    with QuartoModel(DATABASE_URL) as db:
        if request.method == 'POST':
            try:
                db.update(request.form['ID_QUARTO'], request.form['IN_DISPONIVEL'])
            except (DatabaseException, OperationalError, IntegrityError) as err:
                flash(str(err), 'danger')
                return redirect(url_for('quarto.alterar'))
            else:
                db.commit()
                flash('Alterado com sucesso', 'success')
        quartos = db.select_all()
    return render_template('quarto-alterar.html', quartos=quartos)


def deletar():
    with QuartoModel(DATABASE_URL) as db:
        if request.method == 'POST':
            try:
                db.delete(request.form['ID_QUARTO'])
            except (DatabaseException, OperationalError, IntegrityError) as err:
                flash(str(err), 'danger')
                return redirect(url_for('quarto.deletar'))
            else:
                db.commit()
                flash('Deletado com sucesso', 'success')
        quartos = db.select_all()
    return render_template('quarto-deletar.html', quartos=quartos)
