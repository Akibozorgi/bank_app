from datetime import date

import mysql.connector
from model.book import Book


class BorrowRepository:
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

    def borrow_book(self, borrow):
        self.connect()
        self.cursor.execute("INSERT INTO BORROWS (PERSON_ID, BOOK_ID, BORROW_DATE) VALUES (%s, %s, %s)",
                            [borrow.person.id, borrow.book.id, borrow.borrow_date])
        self.connection.commit()
        self.disconnect()

    def return_book(self, borrow):
        self.connect()
        borrow.return_date = date.today()
        self.cursor.execute("UPDATE BORROWS SET RETURN_DATE=%s WHERE ID=%s",
                            [borrow.borrow_date, borrow.id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute()
        borrow_list = self.cursor.fetchall()
        self.disconnect()
        return borrow_list

    def find_by_id(self, book_id):
        self.connect()
        self.cursor.execute()
        borrow = self.cursor.fetchone()
        self.disconnect()
        return borrow

    def find_by_username_and_title (self,username, title):
        self.connect()
        self.cursor.execute()
        borrow_list = self.cursor.fetchall()
        self.disconnect()
        return borrow_list

    def find_non_returned (self):
        self.connect()
        self.cursor.execute()
        borrow_list = self.cursor.fetchall()
        self.disconnect()
        return borrow_list