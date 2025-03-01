class Person:
    def __init__(self, id, name, family, birth_date, username, password):
        self.id = id
        self.name = name
        self.family = family
        self.birth_date = birth_date
        self.username = username
        self.password = password

    def __repr__(self):
        return f"{self.__dict__}"
