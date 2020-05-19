from ..main.models import Database


class Funcionario(Database):
    __tablename__ = 'FUNCIONARIO'
    __tablecolumns__ = ['ID_FUNCIONARIO', 'NU_CPF', 'NO_FUNCIONARIO', 'NU_TELEFONE', 'NO_EMAIL', 'ID_ENDERECO']

    def insert(self, nu_cpf: str, no_funcionario: str, nu_telefone: str, no_email: str, id_endereco: int):
        self.cursor.execute(f'INSERT INTO "{self.__tablename__}" '
                            f'VALUES (NULL, "{nu_cpf}", "{no_funcionario}", "{nu_telefone}", "{no_email}", {id_endereco});'.upper())
        return self.cursor.lastrowid

    def insert_endereco(self, nu_cep: str, no_endereco: str, no_complemento: str, nu_numero: int):
        self.cursor.execute(f'INSERT INTO "ENDERECO" '
                            f'VALUES (NULL, "{nu_cep}", "{no_endereco}", "{no_complemento}", {nu_numero});'.upper())

        return self.cursor.lastrowid

    def update(self, id_: int, nu_telefone: str, no_email: str):
        self.cursor.execute(f'UPDATE "{self.__tablename__}"'
                            f'SET NU_TELEFONE = "{nu_telefone}", NO_EMAIL = "{no_email}" '
                            f'WHERE ID_FUNCIONARIO = {id_};'.upper())

    def update_endereco(self, id_: int, nu_cep: str, no_endereco: str, no_complemento: str, nu_numero: str):
        self.cursor.execute(f'UPDATE "ENDERECO"'
                            f'SET NU_CEP = "{nu_cep}", NO_ENDERECO = "{no_endereco}", '
                            f'    NO_COMPLEMENTO = "{no_complemento}",  NU_NUMERO = "{nu_numero}"'
                            f'WHERE ID_ENDERECO = {id_};'.upper())

    def delete(self, id_: int):
        self.cursor.execute(f'DELETE FROM "{self.__tablename__}" '
                            f'WHERE ID_FUNCIONARIO = {id_};'.upper())

    def delete_endereco(self, id_: int):
        self.cursor.execute(f'DELETE FROM "ENDERECO" '
                            f'WHERE ID_ENDERECO = {id_};'.upper())


class FuncionarioEnderecoView(Database):
    __tablename__ = 'VW_FUNCIONARIO_ENDERECO'
    __tablecolumns__ = ['ID_FUNCIONARIO', 'NU_CPF', 'NO_FUNCIONARIO', 'NU_TELEFONE', 'NO_EMAIL',
                        'ID_ENDERECO', 'NU_CEP', 'NO_ENDERECO', 'NO_COMPLEMENTO', 'NU_NUMERO']
