from flask import make_response, render_template, url_for, abort, redirect

from ..quarto.models import QuartoTipoQuartView, QuartoDisponivelView, QuartoIndisponivelView
from ..funcionario.models import FuncionarioEnderecoView
from ..hospede.models import HospedeEnderecoView
from ..hospedagem.models import HospedagemModel, HospedagemTotalAtivo, HospedagemTotalReceber, HospedagemTotalRecebido
from ...configuration import DATABASE_URL


def home():
    # quantidade total de quartos
    with QuartoTipoQuartView(DATABASE_URL) as db:
        qt_quartos = len(db.select_all())

    # quantidade total de quartos dispoíveis
    with QuartoDisponivelView(DATABASE_URL) as db:
        qt_quartos_disp = len(db.select_all())

    # quantidade total de quartos indispoíveis
    with QuartoIndisponivelView(DATABASE_URL) as db:
        qt_quartos_indisp = len(db.select_all())

    # quantidade de hóspede
    with HospedeEnderecoView(DATABASE_URL) as db:
        qt_hospedes = len(db.select_all())

    # quantidade de hóspede
    with FuncionarioEnderecoView(DATABASE_URL) as db:
        qt_funcionarios = len(db.select_all())

    # quantidade de hospedagem
    with HospedagemModel(DATABASE_URL) as db:
        qt_hospedagem = len(db.select_all())

    # quantidade de hospedagem ativas
    with HospedagemTotalAtivo(DATABASE_URL) as db:
        qt_hospedagem_ativo = db.select_all()[0]['TOTAL_ATIVO']

    # quantidade de hospedagem a receber
    with HospedagemTotalReceber(DATABASE_URL) as db:
        qt_hospedagem_receber = db.select_all()[0]['TOTAL_A_RECEBER']

    # quantidade de hospedagem recebido
    with HospedagemTotalRecebido(DATABASE_URL) as db:
        qt_hospedagem_recebido = db.select_all()[0]['TOTAL_RECEBIDO']

    context = {
        'qt_quartos': qt_quartos,
        'qt_quartos_disp': qt_quartos_disp,
        'qt_quartos_indisp': qt_quartos_indisp,
        'qt_pessoas': qt_hospedes + qt_funcionarios,
        'qt_hospedes': qt_hospedes,
        'qt_funcionarios': qt_funcionarios,
        'qt_hospedagem': qt_hospedagem,
        'qt_hospedagem_ativo': qt_hospedagem_ativo,
        'qt_hospedagem_receber': qt_hospedagem_receber,
        'qt_hospedagem_recebido': qt_hospedagem_recebido
    }

    return render_template('home.html', **context)
