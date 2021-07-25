from .db import get_db


class User:

    def __init__(self, username, password, email=None):
        self.username = username
        self.email = email
        self.password = password

    def log_user(self):
        cursor = get_db().cursor()
        try:
            cursor.execute(
                'SELECT * FROM user WHERE username=?',
                (self.username,))
            user = cursor.fetchone()
            if user:
                return user
        except Exception as ex:
            print(ex)

    def reg_user(self):
        cursor = get_db().cursor()
        conection = get_db()

        try:
            cursor.execute(
                'INSERT INTO user(username, email, password) VALUES(?, ?, ?)',
                (self.username, self.email, self.password))

            conection.commit()
        except Exception as ex:
            print(ex)

    def check_user_by_username(self, username):

        cursor = get_db().cursor()

        try:
            result = cursor.execute('SELECT id FROM user WHERE username=?',
                                    (username,)).fetchone()
            if result:
                return True

        except Exception as ex:
            print(ex)

    @staticmethod
    def check_user_by_id(id):

        cursor = get_db().cursor()

        try:
            user = cursor.execute(
                'SELECT * FROM user WHERE id=?', (id,)).fetchone()
            if user:
                return user
        except Exception as ex:
            print(ex)
