from tkinter import *

from view import view_bank

class BankView:
    def person_show(self):
        self.win.destroy()
        ui = view_bank.personView()

    def card_show(self):
        ui = view_bank.card_view()

    def transaction_show(self):
        ui = view_bank.transaction_View()

    def __init__(self):
        self.win = Tk()
        self.win.title("Main View")
        self.win.geometry("300x300")

        Button(self.win, text="Persons",width=10, command=self.person_show).place(x=20, y = 20)
        Button(self.win, text="Card",width=10, command=self.card_show).place(x=20, y = 80)
        Button(self.win, text="Transaction",width=10, command=self.transaction_show).place(x=20, y = 140)

        self.win.mainloop()