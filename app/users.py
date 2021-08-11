import logging
from werkzeug.security import generate_password_hash, check_password_hash
from .db import get_db


class User:

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

        connection = get_db()
        cursor = connection.cursor()
        
        query = 'SELECT * FROM user WHERE username=?'
        
        try:
            cursor.execute(query, (self.username,))
            user = cursor.fetchone()
            if user:
                return user
        except Exception as ex:
            logging.exception('Error in log_user: ')

    def reg_user(self):
        connection = get_db()
        cursor = connection.cursor()
        
        query = 'INSERT INTO user(username, email, password) VALUES(?, ?, ?)'

        try:
            cursor.execute(query, (self.username, self.email,
                                   self.password_hash))
            connection.commit()
        except Exception as ex:
            logging.exception('Error in reg user: ')

    def check_user_by_username(self, username):
        cursor = get_db().cursor()
        query = 'SELECT id FROM user WHERE username=?'
        try:
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            if result:
                return True

        except Exception as ex:
            logging.exception('Error in check_user_by_username: ')

    @staticmethod
    def check_user_by_id(id):
        cursor = get_db().cursor()
        query = 'SELECT * FROM user WHERE id=?'
        try:
            cursor.execute(query , (id,)).fetchone()
            user = cursor.fetchone()
            if user:
                return user
        except Exception as ex:
            logging.exception('Error in check_user_by_id')
