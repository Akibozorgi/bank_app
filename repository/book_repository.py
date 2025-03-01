import mysql.connector
from model.book import Book


class BookRepository:
    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root123",
            database="mft_library"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, book):
        self.connect()
        self.cursor.execute(
            "INSERT INTO BOOKS (TITLE,WRITER,PUBLISHER,PAGES) VALUES (%s,%s,%s,%s)",
            [book.title, book.writer, book.publisher, book.pages]
        )
        self.connection.commit()
        self.disconnect()

    def edit(self, book):
        self.connect()
        self.cursor.execute(
            "UPDATE BOOKS SET TITLE=%s, WRITER=%s, PUBLISHER=%s, PAGES=%s WHERE B_ID=%s",
            [book.title, book.writer, book.publisher, book.pages, book.id]
        )
        self.connection.commit()
        self.disconnect()

    def remove(self, book_id):
        self.connect()
        self.cursor.execute("DELETE FROM BOOKS WHERE B_ID=%s", [book_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM BOOKS ORDER BY TITLE")
        book_list = self.cursor.fetchall()
        self.disconnect()
        return book_list

    def find_by_id(self, book_id):
        self.connect()
        self.cursor.execute("SELECT * FROM BOOKS WHERE B_ID=%s", [book_id])
        book = self.cursor.fetchone()
        self.disconnect()
        return book

    def find_by_title_and_writer(self, title, writer):
        self.connect()
        self.cursor.execute("SELECT * FROM BOOKS WHERE TITLE LIKE %s AND WRITER LIKE %s", [title + "%", writer + "%"])
        book_list = self.cursor.fetchall()
        self.disconnect()
        return book_list
