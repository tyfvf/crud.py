from tkinter import *
from tkinter import messagebox
import sqlite3

class Functions():

    def clear(self):
        self.number_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.status_var.set('Single')
        self.age_entry.delete(0, END)


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
                city CHAR(40),
                status CHAR(40),
                age INTEGER(3)
            );
        """)
        self.conn.commit()

        self.desconnect()


    def variables(self):
        self.num = self.number_entry.get() 
        self.name = self.name_entry.get() 
        self.phone = self.phone_entry.get() 
        self.city = self.city_entry.get()
        self.status = self.status_var.get()
        self.age = self.age_entry.get() 


    def new_client(self):
        self.variables()

        if self.name == '':
            messagebox.showerror('ERROR!', 'Please insert a name to create a new \nclient in the database =)')
            self.name_entry.focus()
        else:
            self.connect()
            self.cursor.execute("""INSERT INTO clients (name, phone, city, status, age) VALUES (?, ?, ?, ?, ?)""", (self.name, self.phone, self.city, self.status, self.age))
            self.conn.commit()
            self.desconnect()
            self.show_tree()
            self.clear()


    def show_tree(self):
        self.tree.delete(*self.tree.get_children())
        self.connect()
        data = self.cursor.execute("""SELECT num, name, phone, city, status, age FROM clients ORDER BY name ASC;""")
        for i in data:
            self.tree.insert('', END, values=i)
        self.desconnect()


    def double_click(self, event):
        self.clear()
        selected = self.tree.selection()

        for i in selected:
            col1, col2, col3, col4, col5, col6 = self.tree.item(i, 'values')
            self.number_entry.insert(END, col1)
            self.name_entry.insert(END, col2)
            self.phone_entry.insert(END, col3)
            self.city_entry.insert(END, col4)
            self.status_var.set(col5)
            self.age_entry.insert(END, col6)


    def delete_client(self):
        self.variables()
        self.connect()
        self.cursor.execute("""DELETE FROM clients WHERE num = ?""", (self.num,))
        self.conn.commit()
        self.desconnect()
        self.clear()
        self.show_tree()


    def update_client(self):
        self.variables()
        self.connect()
        self.cursor.execute("""UPDATE clients SET name = ?, phone = ?, city = ?, status = ?, age = ? WHERE num = ?""", (self.name, self.phone, self.city, self.status, self.age, self.num))
        self.conn.commit()
        self.desconnect()
        self.clear()
        self.show_tree()


    def search_client(self):
        self.connect()
        self.tree.delete(*self.tree.get_children())
        self.name_entry.insert(END, '%')
        name = self.name_entry.get()
        self.cursor.execute("""SELECT num, name, phone, city, status, age FROM clients WHERE name LIKE '%s' ORDER BY name ASC""" % name)
        data = self.cursor.fetchall()
        for i in data:
            self.tree.insert('', END, values=i)
        self.clear()
        self.desconnect()


    def about(self):
        answer = messagebox.askyesno('About', 
        "This is a CRUD (short for create, read, update, delete) application made in python for desktop, it has some basic functions to help in whatever you need a client database, if needed just change some values for the best suit, it's open source\n\n Did you liked my little project?")

        if answer:
            messagebox.showinfo('Yey', 'Thanks!\nMake sure to give a star at https://github.com/tyfvf/crud.py')
        else:
            messagebox.showinfo('Oh', 
        "=( \n\nMake sure to open a issue or a pull request at https://github.com/tyfvf/crud.py so i can make the project better, your feedback is appreciated ;)")
