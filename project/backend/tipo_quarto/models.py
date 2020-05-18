from ..main.models import Database


class TipoQuartoModel(Database):
    __tablename__ = 'TIPO_QUARTO'
    __tablecolumns__ = ['ID_TIPO_QUARTO', 'NO_TIPO_QUARTO', 'VL_DIARIA']

    def insert(self, no_tipo_quarto: str, vl_diaria: float):
        self._connection.execute(f'INSERT INTO "{self.__tablename__}"'
                                 f'VALUES (NULL, "{no_tipo_quarto}", {vl_diaria});'.upper())

    def update(self, id_: int, vl_diaria: str):
        self._connection.execute(f'UPDATE "{self.__tablename__}"'
                                 f'SET VL_DIARIA = "{vl_diaria}"'
                                 f'WHERE ID_TIPO_QUARTO = {id_};'.upper())

    def delete(self, id_: int):
        self._connection.execute(f'DELETE FROM "{self.__tablename__}"'
                                 f'WHERE ID_TIPO_QUARTO = {id_};'.upper())
