from tkinter import *

class Functions():

    def clear(self):
        self.number_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.city_entry.delete(0, END)