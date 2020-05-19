from ..main.models import Database


class QuartoModel(Database):
    __tablename__ = 'QUARTO'
    __tablecolumns__ = ['ID_QUARTO', 'NU_QUARTO', 'ID_TIPO_QUARTO']

    def insert(self, nu_quarto: int, id_tipo_quarto: int):
        self.cursor.execute(f'INSERT INTO "{self.__tablename__}" '
                            f'VALUES (NULL, {nu_quarto}, {id_tipo_quarto});'.upper())

        return self.cursor.lastrowid

    def delete(self, id_: int):
        self.cursor.execute(f'DELETE FROM "{self.__tablename__}" '
                            f'WHERE ID_QUARTO = {id_};'.upper())


class QuartoTipoQuartView(Database):
    __tablename__ = 'VW_QUARTO_TIPO_QUARTO'
    __tablecolumns__ = ['ID_QUARTO', 'NU_QUARTO', 'ID_TIPO_QUARTO', 'NO_TIPO_QUARTO', 'VL_DIARIA']


class QuartoDisponivelView(Database):
    __tablename__ = 'VW_QUARTO_DISPONIVEL'
    __tablecolumns__ = ['ID_QUARTO', 'NU_QUARTO', 'ID_TIPO_QUARTO', 'NO_TIPO_QUARTO', 'VL_DIARIA']


class QuartoIndisponivelView(Database):
    __tablename__ = 'VW_QUARTO_INDISPONIVEL'
    __tablecolumns__ = ['ID_QUARTO', 'NU_QUARTO', 'ID_TIPO_QUARTO', 'NO_TIPO_QUARTO', 'VL_DIARIA']
