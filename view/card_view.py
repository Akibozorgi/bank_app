from tkinter import *
import tkinter.messagebox as msg
from controller.card_controller import CardController
from validation import card_validator
from view.component.label_and_entry import LabelAndEntry
from view.component.table import Table
from model.card import Card
from repository.card_repository import CardRepository


class CardView:
    def save_click(self):
        status, message = self.controller.save(
            self.id.get(),
            self.bank_name.get(),
            self.card_number.get(),
            self.expire_date.get(),
            self.cvv2.get(),
            self.password.get(),
            self.amount. get(),
            self. person. get(),

        )
        if status:
            msg.showinfo("Saved", message)
        else:
            msg.showerror("Error", message)

            self.reset_form()

    def edit_click(self):
        status, message = self.controller.edit(
            self.id.get(),
            self.bank_name.get(),
            self.card_number.get(),
            self.expire_date.get(),
            self.cvv2.get(),
            self.password.get(),
            self.amount.get(),
            self.person.get(),
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
        self.id.set(0),
        self.bank_name.set(""),
        self.card_number.set(""),
        self.expire_date.set(""),
        self.cvv2.set(""),
        self.password.set(""),
        self.amount.set(""),
        self.person.set(""),
        self.table.clear_table()

    def select_table(self, selected_row):
        # todo : error

        card = Card(*selected_row)
        self.id.set(card.c_id)
        self.bank_name.set(card.bank_name),
        self.card_number.set(card.card_number),
        self.expire_date.set(card.expire_date),
        self.cvv2.set(card.cvv2),
        self.password.set(card.password)
        self.amount.set(card.amount),
        self.person.set(card.person),

    def __init__(self):
        self.controller = CardController()

        self.win = Tk()
        self.win.geometry("950x450")
        self.win.title("Card View")
        self.id = LabelAndEntry(self.win, "Id", 20, 20, IntVar, 80, state="readonly")
        self.bank_name = LabelAndEntry(self.win, "Bank_Name", 20, 60, StringVar, 80)
        self.card_number = LabelAndEntry(self.win, "Card_Number", 20, 100, StringVar, 80)
        self.expire_date = LabelAndEntry(self.win, "Expire_Date", 20, 140, StringVar, 80)
        self.cvv2 = LabelAndEntry(self.win, "Cvv2", 20, 180, StringVar, 80)
        self.password = LabelAndEntry(self.win, "Password", 20, 220, StringVar, 80, show="*")
        self.amount = LabelAndEntry(self.win, "Amount", 20, 260, StringVar, 80,show="*")
        self.person = LabelAndEntry(self.win, "person", 20,300, StringVar, 80)

        Button(self.win, text="Save", width=7, command=self.save_click).place(x=20, y=380)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=85, y=380)
        Button(self.win, text="Remove", width=7, command=self.remove_click).place(x=150, y=380)

        self.table = Table(
            self.win,
            8,
            ["c_id", "bank_name","card_number","expire_date","cvv2", "password","amount", "person"],
            [60, 100, 100, 100, 70, 100, 80, 90],
            230, 20,
            18,
            self.select_table
        )

        self.reset_form()

        self.win.mainloop()
