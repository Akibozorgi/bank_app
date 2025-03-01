from tkinter import *
import tkinter.messagebox as msg

from controller.person_controller import PersonController
from validation.validator import person_validator
from view.component.label_and_entry import LabelAndEntry
from view.component.table import Table

from model.person import Person
from repository.person_repository import PersonRepository


class PersonView:
    def save_click(self):
        status, message = self.controller.save(
            self.name.get(),
            self.family.get(),
            self.birth_date.get(),
            self.username.get(),
            self.password.get(),
        )
        if status:
            msg.showinfo("Saved", message)
        else:
            msg.showerror("Error", message)

            self.reset_form()

    def edit_click(self):
        status, message = self.controller.edit(
            self.id.get(),
            self.name.get(),
            self.family.get(),
            self.birth_date.get(),
            self.username.get(),
            self.password.get()
        )
        if status:
            msg.showinfo("Saved", message)
        else:
            msg.showerror("Error", message)
            self.reset_form()

    def remove_click(self):
        status, message = self.controller.remove(self.id.get())

        if status:
            msg.showinfo("Saved", message)
        else:
            msg.showerror("Error", message)
        self.reset_form()

    def reset_form(self):
        self.id.set(0)
        self.name.set("")
        self.family.set("")
        self.birth_date.set("")
        self.username.set("")
        self.password.set("")
        self.table.clear_table()
        self.table.show_data(self.controller.find_all())

    def select_table(self, selected_row):
        # todo : error
        person = Person(*selected_row)
        self.id.set(person.id)
        self.name.set(person.name)
        self.family.set(person.family)
        self.birth_date.set(person.birth_date)
        self.username.set(person.username)
        self.password.set(person.password)

    def __init__(self):
        self.controller = PersonController()

        self.win = Tk()
        self.win.geometry("710x330")
        self.win.title("Person View")

        self.id = LabelAndEntry(self.win, "Id", 20, 20, IntVar, 65, state="readonly")
        self.name = LabelAndEntry(self.win, "Name", 20, 60, StringVar, 65)
        self.family = LabelAndEntry(self.win, "Family", 20, 100, StringVar, 65)
        self.birth_date = LabelAndEntry(self.win, "BirthDate", 20, 140, StringVar, 65)
        self.username = LabelAndEntry(self.win, "Username", 20, 180, StringVar, 65)
        self.password = LabelAndEntry(self.win, "Password", 20, 220, StringVar, 65, show="*")

        Button(self.win, text="Save", width=7, command=self.save_click).place(x=20, y=280)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=85, y=280)
        Button(self.win, text="Remove", width=7, command=self.remove_click).place(x=150, y=280)

        self.table = Table(
            self.win,
            5,
            ["Id", "Name", "Family", "Birth Date", "Username"],
            [60, 100, 100, 100, 100],
            230, 20,
            13,
            self.select_table
        )

        self.reset_form()

        self.win.mainloop()
