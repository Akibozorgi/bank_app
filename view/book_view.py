from tkinter import *
import tkinter.messagebox as msg

from validation.validator import book_validator
from view.component.label_and_entry import LabelAndEntry
from view.component.table import Table

from model.book import Book
from repository.book_repository import BookRepository


class BookView:
    def save_click(self):
        book = Book(
            self.id.get(),
            self.title.get(),
            self.writer.get(),
            self.publisher.get(),
            self.pages.get(),
        )

        errors = book_validator(book)
        if errors:
            msg.showerror("Error", errors)
        else:
            self.repository.save(book)
            msg.showinfo("Saved", "Book saved")
            self.reset_form()

    def edit_click(self):
        book = Book(
            self.id.get(),
            self.title.get(),
            self.writer.get(),
            self.publisher.get(),
            self.pages.get(),
        )
        errors = book_validator(book)
        if errors:
            msg.showerror("Error", errors)
        else:
            self.repository.save(book)
            msg.showinfo("Edited", "Book edited")
            self.reset_form()

    def remove_click(self):
        self.repository.remove(self.id.get())
        msg.showinfo("Removed", "Book removed")
        self.reset_form()

    def reset_form(self):
        self.id.set(0)
        self.title.set("")
        self.writer.set("")
        self.publisher.set("")
        self.pages.set("")
        self.table.clear_table()
        self.table.show_data(self.repository.find_all())

    def select_table(self, selected_row):
        book = Book(*selected_row)
        self.id.set(book.id)
        self.title.set(book.title)
        self.writer.set(book.writer)
        self.publisher.set(book.publisher)
        self.pages.set(book.pages)

    def __init__(self):
        self.repository = BookRepository()

        self.win = Tk()
        self.win.geometry("680x330")
        self.win.title("Book View")


        self.id = LabelAndEntry(self.win,"Id",20,20,IntVar, 65, state="readonly" )
        self.title = LabelAndEntry(self.win,"Title",20,60,StringVar,65 )
        self.writer = LabelAndEntry(self.win,"Writer",20,100,StringVar,65 )
        self.publisher = LabelAndEntry(self.win,"Publisher",20,140,StringVar,65 )
        self.pages = LabelAndEntry(self.win,"Pages",20,180,StringVar,65 )

        Button(self.win , text="Save",width=7, command=self.save_click).place(x=20, y =280)
        Button(self.win , text="Edit",width=7, command=self.edit_click).place(x=85, y =280)
        Button(self.win , text="Remove",width=7, command=self.remove_click).place(x=150, y =280)

        self.table = Table(
            self.win,
            5,
            ["Id","Title","Writer","Publisher","Pages"],
            [60,100,100,100,60],
            230,20,
            13,
            self.select_table
        )

        self.reset_form()

        self.win.mainloop()