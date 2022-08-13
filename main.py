from tkinter import *


class Application():
    def __init__(self):
        self.root = Tk()
        self.screen()
        self.frames()
        self.widgets_frame1()
        self.root.mainloop()


    def screen(self):
        self.root.geometry('800x500+500+200')
        self.root.title('crud.py')
        self.root.resizable(True, True)
        self.root.config(bg='#87BDFF')
        self.root.maxsize(width=1000, height=600)
        self.root.minsize(width=600, height=400)


    def frames(self):
        self.frame1 = Frame(self.root, bg='#6CABFA', bd=4, highlightbackground='#396EAD', highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.45)

        self.frame2 = Frame(self.root, bg='#6CABFA', bd=4, highlightbackground='#396EAD', highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.50, relwidth=0.96, relheight=0.47)


    def widgets_frame1(self):
        
        # Number
        self.lb_number = Label(self.frame1, text='Number', bg='#6CABFA')
        self.lb_number.place(relx=0.02, rely=0.02, relwidth=0.08, relheight=0.08)

        self.number_entry = Entry(self.frame1)
        self.number_entry.place(relx=0.02, rely=0.12, relwidth=0.08, relheight=0.08)

        # Name
        self.lb_name = Label(self.frame1, text='Name', bg='#6CABFA')
        self.lb_name.place(relx=0.02, rely=0.35, relwidth=0.08, relheight=0.08)

        self.name_entry = Entry(self.frame1)
        self.name_entry.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.08)

        # Cellphone
        self.lb_cellphone = Label(self.frame1, text='Cellphone', bg='#6CABFA')
        self.lb_cellphone.place(relx=0.02, rely=0.6, relwidth=0.08, relheight=0.08)

        self.cellphone_entry = Entry(self.frame1)
        self.cellphone_entry.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.08)

        # City
        self.lb_city = Label(self.frame1, text='City', bg='#6CABFA')
        self.lb_city.place(relx=0.5, rely=0.6, relwidth=0.08, relheight=0.08)

        self.city_entry = Entry(self.frame1)
        self.city_entry.place(relx=0.58, rely=0.6, relwidth=0.32, relheight=0.08)

        # Clear
        self.bt_clear = Button(self.frame1, text='Clear', bg='#AD7E28', fg='white', activebackground='#FAC76B', activeforeground='white', font=('Verdana', 9, 'bold'))
        self.bt_clear.place(relx=0.2, rely=0.08, relheight=0.13, relwidth=0.1)

        # Search
        self.bt_search = Button(self.frame1, text='Search', bg='#AD7E28', fg='white', activebackground='#FAC76B', activeforeground='white', font=('Verdana', 9, 'bold'))
        self.bt_search.place(relx=0.3, rely=0.08, relheight=0.13, relwidth=0.1)

        # Create
        self.bt_search = Button(self.frame1, text='Create', bg='#AD7E28', fg='white', activebackground='#FAC76B', activeforeground='white', font=('Verdana', 9, 'bold'))
        self.bt_search.place(relx=0.6, rely=0.08, relheight=0.13, relwidth=0.1)

        # Update
        self.bt_search = Button(self.frame1, text='Update', bg='#AD7E28', fg='white', activebackground='#FAC76B', activeforeground='white', font=('Verdana', 9, 'bold'))
        self.bt_search.place(relx=0.7, rely=0.08, relheight=0.13, relwidth=0.1)

        # Delete
        self.bt_search = Button(self.frame1, text='Delete', bg='#AD7E28', fg='white', activebackground='#FAC76B', activeforeground='white', font=('Verdana', 9, 'bold'))
        self.bt_search.place(relx=0.8, rely=0.08, relheight=0.13, relwidth=0.1)


Application()