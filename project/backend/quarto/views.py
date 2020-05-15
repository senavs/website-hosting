from sqlite3 import OperationalError

from flask import make_response, render_template, url_for, abort, redirect, flash, request

from .models import ViewQuartoTipoQuarto, ModelQuarto, ModelTipoQuarto
from ..main.models import DatabaseException
from ...configuration import DATABASE_URL


def listar():
    with ViewQuartoTipoQuarto(DATABASE_URL) as db:
        quartos = db.select_all()
    return render_template('quarto-listar.html', title='Listar Quartos', quartos=quartos)


def cadastrar():
    if request.method == 'POST':
        with ModelQuarto(DATABASE_URL) as db:
            try:
                db.insert(request.form['nu_quarto'], request.form['in_disponivel'], request.form['id_tipo_quarto'])
            except (DatabaseException, OperationalError) as err:
                flash(str(err), 'danger')
            else:
                db.commit()
                flash('Quarto alterado com sucesso', 'success')
            return redirect(url_for('quarto.cadastrar'))
    with ModelTipoQuarto(DATABASE_URL) as db:
        tipo_quarto = db.select_all()
    return render_template('quarto-cadastrar.html', title='Cadastrar Quarto', tipo_quarto=tipo_quarto)


def alterar_disponibilizade():
    if request.method == 'POST':
        with ModelQuarto(DATABASE_URL) as db:
            try:
                db.update_in_disponivel(request.form['nu_quarto'], request.form['in_disponivel'])
            except (DatabaseException, OperationalError) as err:
                flash(str(err), 'danger')
            else:
                db.commit()
                flash('Quarto alterado com sucesso', 'success')
        return redirect(url_for('quarto.alterar-disponibilizade'))
    with ModelQuarto(DATABASE_URL) as db:
        quartos = db.select_all()
    return render_template('quarto-alterar-disponibilizade.html', title='Alterar disponibilidade', quartos=quartos)


def deletar():
    if request.method == 'POST':
        with ModelQuarto(DATABASE_URL) as db:
            db.delete(request.form['nu_quarto'])
            db.commit()
            flash('Quarto alterado com sucesso', 'success')
        return redirect(url_for('quarto.deletar'))
    with ModelQuarto(DATABASE_URL) as db:
        quartos = db.select_all()
    return render_template('quarto-deletar.html', title='Deletar quarto', quartos=quartos)