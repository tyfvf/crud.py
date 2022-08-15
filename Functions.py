from tkinter import *
from tkinter import messagebox
import sqlite3

class Functions():

    def clear(self):
        self.number_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.city_entry.delete(0, END)


    def connect(self):
        self.conn = sqlite3.connect('clients.db')
        self.cursor = self.conn.cursor()


    def desconnect(self):
        self.conn.close()


    def tables(self):
        self.connect()

        # Clients table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                num INTEGER PRIMARY KEY,
                name CHAR(40) NOT NULL,
                phone INTEGER(20),
                city CHAR(40)
            );
        """)
        self.conn.commit()

        self.desconnect()


    def variables(self):
        self.num = self.number_entry.get() 
        self.name = self.name_entry.get() 
        self.phone = self.phone_entry.get() 
        self.city = self.city_entry.get() 


    def new_client(self):
        self.variables()

        if self.name == '':
            messagebox.showerror('ERROR!', 'Please insert a name to create a new \nclient in the database =)')
            self.name_entry.focus()
        else:
            self.connect()
            self.cursor.execute("""INSERT INTO clients (name, phone, city) VALUES (?, ?, ?)""", (self.name, self.phone, self.city))
            self.conn.commit()
            self.desconnect()
            self.show_tree()
            self.clear()


    def show_tree(self):
        self.tree.delete(*self.tree.get_children())
        self.connect()
        data = self.cursor.execute("""SELECT num, name, phone, city FROM clients ORDER BY name ASC;""")
        for i in data:
            self.tree.insert('', END, values=i)
        self.desconnect()
