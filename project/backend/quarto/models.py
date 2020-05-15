from project.backend.main.models import Database, DatabaseException


class ModelQuarto(Database):
    __tablename__ = 'QUARTO'
    __tablecolumns__ = ['ID', 'NU_QUARTO', 'IN_DISPONIVEL', 'ID_TIPO_QUARTO']

    def insert(self, nu_quarto: int, in_disponivel: int, id_tipo_quarto):
        if self.select_all_by(nu_quarto=nu_quarto):
            raise DatabaseException('Quarto já cadastrado')
        self._connection.execute(f'INSERT INTO "{self.__tablename__}" VALUES (NULL, {nu_quarto}, {in_disponivel}, {id_tipo_quarto})')

    def update_in_disponivel(self, nu_quarto: int, in_disponivel: int):
        self._connection.execute(f'UPDATE "{self.__tablename__}" SET "IN_DISPONIVEL" = {in_disponivel} WHERE NU_QUARTO = {int(nu_quarto)}')

    def delete(self, nu_quarto: int):
        self._connection.execute(f'DELETE FROM "{self.__tablename__}" WHERE NU_QUARTO = {int(nu_quarto)}')


class ModelTipoQuarto(Database):
    __tablename__ = 'TIPO_QUARTO'
    __tablecolumns__ = ['ID', 'NO_TIPO_QUARTO', 'VL_DIARIA']


class ViewQuartoTipoQuarto(Database):
    __tablename__ = 'VW_QUARTO_TIPO_QUARTO'
    __tablecolumns__ = ['ID', 'NU_QUARTO', 'IN_DISPONIVEL', 'ID_TIPO_QUARTO', 'NO_TIPO_QUARTO', 'VL_DIARIA']


class ViewQuartoDisponivel(Database):
    __tablename__ = 'VW_QUARTO_DISPONIVEL'
    __tablecolumns__ = ['ID', 'NU_QUARTO', 'IN_DISPONIVEL', 'ID_TIPO_QUARTO', 'NO_TIPO_QUARTO', 'VL_DIARIA']


class ViewQuartoIndisponivel(Database):
    __tablename__ = 'VW_QUARTO_INDISPONIVEL'
    __tablecolumns__ = ['ID', 'NU_QUARTO', 'IN_DISPONIVEL', 'ID_TIPO_QUARTO', 'NO_TIPO_QUARTO', 'VL_DIARIA']
