import logging
from werkzeug.security import generate_password_hash, check_password_hash
from .db import get_db


class User:
    connection = None
    cursor = None

    def __init__(self, username, password, email=None):
        self.username = username
        self.email = email
        self.password = password

    @property
    def password(self):
        raise AttributeError('This property can\'t be read')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def log_user(self):
        self.connection = get_db()
        self.cursor = self.connection.cursor()
        query = 'SELECT * FROM user WHERE username=?'

        try:
            self.cursor.execute(query, (self.username,))
            user = self.cursor.fetchone()

            if user:
                return user
        except Exception as ex:
            logging.exception('Error in log_user: ')


    def reg_user(self) -> None:
        self.connection = get_db()
        self.cursor = self.connection.cursor()
        query = 'INSERT INTO user(username, email, password) VALUES(?, ?, ?)'

        try:
            self.cursor.execute(query, (self.username, self.email,
                                        self.password_hash))
            self.connection.commit()
            return
        except Exception as ex:
            logging.exception('Error in reg user: ')


    def check_user_by_username(self, username: str) -> bool:
        self.cursor = get_db().cursor()
        query = 'SELECT id FROM user WHERE username=?'

        try:
            self.cursor.execute(query, (username,))
            result = self.cursor.fetchone()
            if result:
                return True

        except Exception as ex:
            logging.exception('Error in check_user_by_username: ')


    @staticmethod
    def check_user_by_id(user_id: int) -> tuple:
        User.cursor = get_db().cursor()
        query = 'SELECT * FROM user WHERE id=?'

        try:
            User.cursor.execute(query, (user_id,))
            user = User.cursor.fetchone()
            if user:
                return user
        except Exception as ex:
            logging.exception('Error in check_user_by_id')
