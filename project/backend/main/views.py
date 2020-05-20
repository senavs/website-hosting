from flask import make_response, render_template, url_for, abort, redirect

from ..quarto.models import QuartoTipoQuartView, QuartoDisponivelView, QuartoIndisponivelView
from ..funcionario.models import FuncionarioEnderecoView, RankFuncionarioView
from ..hospede.models import HospedeEnderecoView
from ..hospedagem.models import HospedagemModel, HospedagemTotalAtivo, HospedagemTotalReceber, HospedagemTotalRecebido
from ...configuration import DATABASE_URL


def home():
    # quantidade total de quartos
    with QuartoTipoQuartView(DATABASE_URL) as db:
        qt_quartos = len(db.select_all())

    # quantidade total de quartos dispoíveis
    with QuartoDisponivelView(DATABASE_URL) as db:
        nu_quartos_disp = [quarto['NU_QUARTO'] for quarto in db.select_all()]
        qt_quartos_disp = len(nu_quartos_disp)

    # quantidade total de quartos indispoíveis
    with QuartoIndisponivelView(DATABASE_URL) as db:
        nu_quartos_indisp = [quarto['NU_QUARTO'] for quarto in db.select_all()]
        qt_quartos_indisp = len(nu_quartos_indisp)

    # quantidade de hóspede
    with HospedeEnderecoView(DATABASE_URL) as db:
        qt_hospedes = len(db.select_all())

    # quantidade de hóspede
    with FuncionarioEnderecoView(DATABASE_URL) as db:
        qt_funcionarios = len(db.select_all())

    # quantidade de hospedagem
    with HospedagemModel(DATABASE_URL) as db:
        qt_hospedagem = len(db.select_all())
        ids_hospedagem_ativa = [hospedagem['ID_HOSPEDAGEM'] for hospedagem in db.select_all_by(in_ativo=1)]

    # quantidade de hospedagem ativas
    with HospedagemTotalAtivo(DATABASE_URL) as db:
        qt_hospedagem_ativo = db.select_all()[0]['TOTAL_ATIVO']

    # quantidade de hospedagem a receber
    with HospedagemTotalReceber(DATABASE_URL) as db:
        qt_hospedagem_receber = db.select_all()[0]['TOTAL_A_RECEBER']

    # quantidade de hospedagem recebido
    with HospedagemTotalRecebido(DATABASE_URL) as db:
        qt_hospedagem_recebido = db.select_all()[0]['TOTAL_RECEBIDO']

    # rank de funcionarios
    with RankFuncionarioView(DATABASE_URL) as db:
        rank_funcionario = db.select_all()

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
        'qt_hospedagem_recebido': qt_hospedagem_recebido,
        'ids_hospedagem_ativa': ids_hospedagem_ativa,
        'nu_quartos_disp': nu_quartos_disp,
        'nu_quartos_indisp': nu_quartos_indisp,
        'rank_funcionario': rank_funcionario
    }

    return render_template('home.html', **context)
