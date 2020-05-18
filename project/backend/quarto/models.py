from ..main.models import Database


class QuartoModel(Database):
    __tablename__ = 'QUARTO'
    __tablecolumns__ = ['ID_QUARTO', 'NU_QUARTO', 'IN_DISPONIVEL', 'ID_TIPO_QUARTO']

    def insert(self, nu_quarto: int, in_disponivel: int, id_tipo_quarto: int):
        self._connection.execute(f'INSERT INTO "{self.__tablename__}" '
                                 f'VALUES (NULL, {nu_quarto}, {in_disponivel}, {id_tipo_quarto});'.upper())

    def update(self, id_: int, in_disponivel: str):
        self._connection.execute(f'UPDATE "{self.__tablename__}"'
                                 f'SET IN_DISPONIVEL = {in_disponivel} '
                                 f'WHERE ID_QUARTO = {id_};'.upper())

    def delete(self, id_: int):
        self._connection.execute(f'DELETE FROM "{self.__tablename__}" '
                                 f'WHERE ID_QUARTO = {id_};'.upper())


class QuartoTipoQuartView(Database):
    __tablename__ = 'VW_QUARTO_TIPO_QUARTO'
    __tablecolumns__ = ['ID_QUARTO', 'NU_QUARTO', 'IN_DISPONIVEL', 'ID_TIPO_QUARTO', 'NO_TIPO_QUARTO', 'VL_DIARIA']


class QuartoDisponivelView(Database):
    __tablename__ = 'VW_QUARTO_DISPONIVEL'
    __tablecolumns__ = ['ID_QUARTO', 'NU_QUARTO', 'IN_DISPONIVEL', 'ID_TIPO_QUARTO', 'NO_TIPO_QUARTO', 'VL_DIARIA']


class QuartoIndisponivelView(Database):
    __tablename__ = 'VW_QUARTO_INDISPONIVEL'
    __tablecolumns__ = ['ID_QUARTO', 'NU_QUARTO', 'IN_DISPONIVEL', 'ID_TIPO_QUARTO', 'NO_TIPO_QUARTO', 'VL_DIARIA']
