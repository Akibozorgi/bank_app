from tkinter import Tk

from view import *
from view.main import MainView


class PersonView:
    def return_main(self):
        self.win.destroy()
        ui = MainView()

    def __init__(self):
        self.win = Tk()
        self.win.protocol("WM_DELETE_WINDOW", self.return_main)

        self.win.title("Person View")

        self.win.mainloop()