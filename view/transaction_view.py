
from tkinter import *
import tkinter.messagebox as msg
from controller.transaction_controller import TransactionController
from validation import transaction_validator
from view.component.label_and_entry import LabelAndEntry
from view.component.table import Table
from model.transaction import Transaction
from repository.transaction_repository import TransactionRepository

class TransactionView:
    def save_click(self):
        status, message = self.controller.save(
            self.t_id.get(),
            self.amount.get(),
            self.date_time.get(),
            self.sender.get(),
            self.receiver.get(),
        )
        if status:
            msg.showinfo("Saved", message)
        else:
            msg.showerror("Error", message)

            self.reset_form()

    def edit_click(self):
        status, message = self.controller.edit(
            self.t_id.get(),
            self.amount.get(),
            self.date_time.get(),
            self.sender.get(),
            self.receiver.get(),
        )
        if status:
            msg.showinfo("Saved", message)
        else:
            msg.showerror("Error", message)
            self.reset_form()

    def remove_click(self):
        status, message = self.controller.remove(self.t_id.get())

        if status:
            msg.showinfo("Saved", message)
        else:
            msg.showerror("Error", message)
        self.reset_form()

    def reset_form(self):
        self.t_id.set(None)
        self.amount.set("")
        self.date_time.set("")
        self.sender.set("")
        self.receiver.set("")
        self.table.clear_table()


    def select_table(self, selected_row):
        # todo : error
        transaction = Transaction(*selected_row)
        self.t_id.set(transaction.id)
        self.amount.set(transaction.amount)
        self.date_time.set(transaction.date_time)
        self.sender.set(transaction.sender)
        self.receiver.set(transaction.receiver)

    def __init__(self):
        self.controller = TransactionController()

        self.win = Tk()
        self.win.geometry("710x330")
        self.win.title("Transaction View")

        self.t_id = LabelAndEntry(self.win, "Id", 20, 20, IntVar, 65, state="readonly")
        self.amount = LabelAndEntry(self.win, "Amount", 20, 60, StringVar, 65)
        self.date_time = LabelAndEntry(self.win, "Date_Time", 20, 100, StringVar, 65)
        self.sender = LabelAndEntry(self.win, "Sender", 20, 140, StringVar, 65)
        self.receiver = LabelAndEntry(self.win, "Receiver", 20, 180, StringVar, 65)

        Button(self.win, text="Save", width=7, command=self.save_click).place(x=20, y=280)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=85, y=280)
        Button(self.win, text="Remove", width=7, command=self.remove_click).place(x=150, y=280)

        self.table = Table(
            self.win,
            5,
            ["T_Id", "Amount", "Date_Time", "Sender", "Receiver"],
            [60, 100, 100, 100, 100],
            230, 20,
            13,
            self.select_table
        )

        self.reset_form()

        self.win.mainloop()

