from tkinter import *
import tkinter.messagebox as msg

from model.book import Book
from model.borrow import Borrow
from repository.book_repository import BookRepository
from repository.borrow_repository import BorrowRepository
from view.component.label_and_entry import LabelAndEntry
from view.component.table import Table

from model.person import Person
from repository.person_repository import PersonRepository


class BorrowView:
    def reset_form(self):
        self.person_table.clear_table()
        self.person_table.show_data(self.person_repo.find_all())

        self.book_table.clear_table()
        self.book_table.show_data(self.book_repo.find_all())

    def select_person(self, selected_row):
        self.person = Person(*self.person_repo.find_by_id(selected_row[0]))

    def select_book(self, selected_row):
        self.book = Book(*self.book_repo.find_by_id(selected_row[0]))

    def save_borrow(self):
        borrow = Borrow(None, self.person, self.book)
        self.borrow_repo.borrow_book(borrow)
        msg.showinfo("Borrow", f"Borrow Saved {borrow} successfully")

    def __init__(self):
        self.person_repo = PersonRepository()
        self.book_repo = BookRepository()
        self.borrow_repo = BorrowRepository()
        self.person = None
        self.book = None

        self.win = Tk()
        self.win.geometry("700x450")
        self.win.title("Borrow View")

        self.person_table = Table(
            self.win,
            3,
            ["Id", "Name", "Family"],
            [60, 100, 100],
            20, 20,
            13,
            self.select_person
        )

        self.name = LabelAndEntry(self.win, "Name", 20, 330, StringVar, 70)
        self.family = LabelAndEntry(self.win, "Family", 20, 370, StringVar, 70)

        self.book_table = Table(
            self.win,
            4,
            ["Id", "Title", "Writer", "Publisher"],
            [60, 100, 100, 100],
            300, 20,
            13,
            self.select_book
        )
        self.title = LabelAndEntry(self.win, "Title", 300, 330, StringVar, 70)

        Button(self.win, text="Borrow", width=15, command=self.save_borrow).place(x=250, y=400)

        self.reset_form()

        self.win.mainloop()
