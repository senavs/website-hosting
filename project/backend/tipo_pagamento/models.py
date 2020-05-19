from ..main.models import Database


class TipoPagamentoModel(Database):
    __tablename__ = 'TIPO_PAGAMENTO'
    __tablecolumns__ = ['ID_TIPO_PAGAMENTO', 'NO_TIPO_PAGAMENTO']

    def insert(self, no_tipo_pagamento: str):
        self.cursor.execute(f'INSERT INTO "{self.__tablename__}" '
                            f'VALUES (NULL, "{no_tipo_pagamento}"); '.upper())

        return self.cursor.lastrowid

    def update(self, id_: int, no_tipo_pagamento: str):
        self.cursor.execute(f'UPDATE "{self.__tablename__}" '
                            f'SET NO_TIPO_PAGAMENTO = "{no_tipo_pagamento}" '
                            f'WHERE ID_TIPO_PAGAMENTO = {id_}; '.upper())

    def delete(self, id_: int):
        self.cursor.execute(f'DELETE FROM "{self.__tablename__}" '
                            f'WHERE ID_TIPO_PAGAMENTO = {id_}; '.upper())
