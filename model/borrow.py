from datetime import date


class Borrow:
    def __init__(self, id, person, book, borrow_date=date.today(), return_date=None):
        self.id = id
        self.person = person
        self.book = book
        self.borrow_date = borrow_date
        self.return_date = return_date

    def __repr__(self):
        return f"{self.__dict__}"
