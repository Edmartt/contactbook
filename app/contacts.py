from db import get_db

class Contact:

    def __init__(self, name, email, phone, user_id=None):
        self._name = name
        self._phone = phone
        self._user_id = user_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self.phone = phone
