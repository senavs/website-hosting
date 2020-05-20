from ..main.models import Database


class HospedagemModel(Database):
    __tablename__ = 'HOSPEDAGEM'
    __tablecolumns__ = ['ID_HOSPEDAGEM', 'ID_FUNCIONARIO', 'ID_QUARTO', 'ID_TIPO_PAGAMENTO',
                        'ID_HOSPEDE_TITULAR', 'ID_HOSPEDE_ACOMPANHANTE_1', 'ID_HOSPEDE_ACOMPANHANTE_2', 'ID_HOSPEDE_ACOMPANHANTE_3',
                        'IN_ATIVA', 'DT_ENTRADA', 'NU_NOITE', 'VL_HOSPEDAGEM']

    def insert(self, id_funcionario: int, id_quarto: int, id_tipo_pagamento: int, id_hospede_titular: int,
               id_hospede_acompanhante_1: int, id_hospede_acompanhante_2: int, id_hospede_acompanhante_3: int,
               dt_entrada: str, nu_noite: int):
        self.cursor.execute(f'INSERT INTO "{self.__tablename__}" '
                            f'VALUES (NULL, {id_funcionario}, {id_quarto}, {id_tipo_pagamento}, '
                            f'              {id_hospede_titular}, {id_hospede_acompanhante_1}, {id_hospede_acompanhante_2}, {id_hospede_acompanhante_3}, '
                            f'              1, "{dt_entrada}", {nu_noite}, NULL) ;'.upper())
        return self.cursor.lastrowid

    def update(self, id_: int, in_ativo: int):
        self.cursor.execute(f'UPDATE "{self.__tablename__}" '
                            f'SET IN_ATIVO = {in_ativo} '
                            f'WHERE ID_HOSPEDAGEM = {id_} ;'.upper())


class HospedagemDetalhadaView(Database):
    __tablename__ = 'VW_HOSPEDAGEM_COMPLETA'
    __tablecolumns__ = ['ID_HOSPEDAGEM', 'ID_FUNCIONARIO', 'NU_CPF_FUNCIONARIO', 'NO_FUNCIONARIO', 'ID_QUARTO', 'NU_QUARTO', 'ID_TIPO_QUARTO', 'NO_TIPO_QUARTO',
                        'VL_DIARIA', 'ID_TIPO_PAGAMENTO', 'NO_TIPO_PAGAMENTO', 'ID_HOSPEDE_TITULAR', 'NU_CPF_TITULAR', 'NO_HOSPEDE_TITULAR',
                        'ID_HOSPEDE_ACOMPANHANTE_1', 'NU_CPF_ACOMPANHANTE_1', 'NO_HOSPEDE_ACOMPANHANTE_1', 'ID_HOSPEDE_ACOMPANHANTE_2', 'NU_CPF_ACOMPANHANTE_2',
                        'NO_HOSPEDE_ACOMPANHANTE_2', 'ID_HOSPEDE_ACOMPANHANTE_3', 'NU_CPF_ACOMPANHANTE_3', 'NO_HOSPEDE_ACOMPANHANTE_3', 'IN_ATIVO',
                        'DT_ENTRADA', 'NU_NOITE', 'VL_HOSPEDAGEM']


class HospedeDisponivelHospedagem(Database):
    __tablename__ = 'VW_HOSPEDE_DISPONIVEL_HOSPEDAGEM'
    __tablecolumns__ = ['ID_HOSPEDE', 'NU_CPF', 'NO_HOSPEDE', 'IN_ATIVO']


class HospedagemTotalReceber(Database):
    __tablename__ = 'VW_HOSPEDAGEM_TOTAL_A_RECEBER'
    __tablecolumns__ = ['TOTAL_A_RECEBER']


class HospedagemTotalRecebido(Database):
    __tablename__ = 'VW_HOSPEDAGEM_TOTAL_RECEBIDO'
    __tablecolumns__ = ['TOTAL_RECEBIDO']


class HospedagemTotalAtivo(Database):
    __tablename__ = 'VW_HOSPEDAGEM_TOTAL_ATIVO'
    __tablecolumns__ = ['TOTAL_ATIVO']
