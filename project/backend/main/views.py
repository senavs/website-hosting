from flask import make_response, render_template, url_for, abort, redirect

from ..quarto.models import QuartoTipoQuartView, QuartoDisponivelView, QuartoIndisponivelView
from ...configuration import DATABASE_URL


def home():
    # quantidade total de quartos
    with QuartoTipoQuartView(DATABASE_URL) as db:
        qt_quartos = db.select_all()
        qt_quartos = len(qt_quartos)

    # quantidade total de quartos dispoíveis
    with QuartoDisponivelView(DATABASE_URL) as db:
        qt_quartos_disp = db.select_all()
        qt_quartos_disp = len(qt_quartos_disp)

    # quantidade total de quartos indispoíveis
    with QuartoIndisponivelView(DATABASE_URL) as db:
        qt_quartos_indisp = db.select_all()
        qt_quartos_indisp = len(qt_quartos_indisp)

    context = {
        'qt_quartos': qt_quartos,
        'qt_quartos_disp': qt_quartos_disp,
        'qt_quartos_indisp': qt_quartos_indisp
    }
    print(context)
    return render_template('home.html', **context)
