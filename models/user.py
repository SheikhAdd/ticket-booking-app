import re

class User:
    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name.strip().capitalize()
        self.last_name = last_name.strip().capitalize()
        self.phone = phone.strip()

    def is_valid(self):
        return self._validate_name(self.first_name) and \
               self._validate_name(self.last_name) and \
               self._validate_phone(self.phone)

    @staticmethod
    def _validate_name(name):
        return name.isalpha() and len(name) >= 2

    @staticmethod
    def _validate_phone(phone):
        pattern = r"^\+7\d{3}-\d{3}-\d{2}-\d{2}$"
        return re.match(pattern, phone)
