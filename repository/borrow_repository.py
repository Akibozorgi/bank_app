from datetime import date

import mysql.connector
from model.book import Book
from model.borrow import Borrow
from model.person import Person


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

    def convert_borrow_tuple_to_object(self, borrow_tuple):
        person = Person(*borrow_tuple[5:11])
        book = Book(*borrow_tuple[11:])
        borrow = Borrow(borrow_tuple[0], person, book, borrow_tuple[1], borrow_tuple[2])
        return borrow

    def borrow_book(self, borrow):
        self.connect()
        self.cursor.execute("INSERT INTO BORROWS (PERSON_ID, BOOK_ID, BORROW_DATE) VALUES (%s, %s, %s)",
                            [borrow.person.id, borrow.book.id, borrow.borrow_date])
        self.connection.commit()
        self.disconnect()

    def return_book(self, borrow_id):
        self.connect()
        self.cursor.execute("UPDATE BORROWS SET RETURN_DATE=%s WHERE ID=%s",
                            [date.today(), borrow_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM BORROW_REPORT")
        borrow_list = list(map(self.convert_borrow_tuple_to_object , self.cursor.fetchall()))
        self.disconnect()
        return borrow_list

    def find_by_person_id(self, person_id):
        self.connect()
        self.cursor.execute("SELECT * FROM BORROWS WHERE PERSON_ID=%s", [person_id])
        borrow_list = list(map(self.convert_borrow_tuple_to_object , self.cursor.fetchall()))
        self.disconnect()
        return borrow_list


    def find_by_book_id(self, book_id):
        self.connect()
        self.cursor.execute("SELECT * FROM BORROW_REPORT WHERE BOOK_ID=%s", [book_id])
        borrow_list = list(map(self.convert_borrow_tuple_to_object, self.cursor.fetchall()))
        self.disconnect()
        return borrow_list

    def find_by_username_and_title (self,username, title):
        self.connect()
        self.cursor.execute("SELECT * FROM BORROW_REPORT WHERE USERNAME=%s AND TITLE=%s", [username, title])
        borrow_list = list(map(self.convert_borrow_tuple_to_object, self.cursor.fetchall()))
        self.disconnect()
        return borrow_list

    def find_all_non_returned (self):
        self.connect()
        self.cursor.execute("SELECT * FROM BORROW_REPORT WHERE RETURN_DATE IS NULL")
        borrow_list = list(map(self.convert_borrow_tuple_to_object, self.cursor.fetchall()))
        self.disconnect()
        return borrow_list

    def find_non_returned_by_username (self, username):
        self.connect()
        self.cursor.execute("SELECT * FROM BORROW_REPORT WHERE USERNAME=%s AND RETURN_DATE IS NULL", [username])
        borrow_list = list(map(self.convert_borrow_tuple_to_object, self.cursor.fetchall()))
        self.disconnect()
        return borrow_list