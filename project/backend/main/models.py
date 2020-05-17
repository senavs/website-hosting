import sqlite3
from sqlite3 import ProgrammingError
from typing import Iterable


# NOT USING ORM BECAUSE OF THE PROJECT REQUIREMENTS
class Database:
    _connection = None
    __tablename__ = None
    __tablecolumns__ = []

    def __init__(self, url: str):
        self.url = url

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def open(self):
        self._connection = sqlite3.connect(self.url)

    def close(self):
        self._connection.close()

    def commit(self):
        self._connection.commit()

    def cursor_to_dict(self, cursors: Iterable):
        return [dict(zip(self.__tablecolumns__, cursor)) for cursor in cursors]

    def select_all(self):
        if self._connection:
            return self.cursor_to_dict(self._connection.execute(f'SELECT * FROM {self.__tablename__};'))
        raise ProgrammingError('ProgrammingError: Cannot operate on a closed database.')

    def select_all_by(self, and_operator=True, **kwargs):
        if self._connection:
            if and_operator:
                filters = ' AND '.join(f'{key} = {value}'.upper() for key, value in kwargs.items())
            else:
                filters = ' OR '.join(f'{key} = {value}'.upper() for key, value in kwargs.items())
            return self.cursor_to_dict(self._connection.execute(f'SELECT * FROM {self.__tablename__} WHERE {filters};'))
        raise ProgrammingError('ProgrammingError: Cannot operate on a closed database.')


class DatabaseException(Exception):
    """Base class to database exception"""
