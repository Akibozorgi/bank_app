class Book:
    def __init__(self, id, title, writer,publisher, pages):
        self.id = id
        self.title = title
        self.writer = writer
        self.publisher = publisher
        self.pages = pages

    def __repr__(self):
        return f"{self.__dict__}"
