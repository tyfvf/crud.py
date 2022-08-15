from tkinter import *
from tkinter import ttk
from Functions import Functions


class Application(Functions):
    def __init__(self):
        self.root = Tk()
        self.screen()
        self.frames()
        self.widgets_frame1()
        self.treeview()
        self.tables()
        self.show_tree()
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
        self.lb_number = Label(self.frame1, text='Number', bg='#6CABFA', font=('Verdana', 8, 'bold'))
        self.lb_number.place(relx=0.02, rely=0.02, relwidth=0.08, relheight=0.08)

        self.number_entry = Entry(self.frame1)
        self.number_entry.place(relx=0.02, rely=0.12, relwidth=0.08, relheight=0.08)

        # Name
        self.lb_name = Label(self.frame1, text='Name', bg='#6CABFA', font=('Verdana', 8, 'bold'))
        self.lb_name.place(relx=0.02, rely=0.35, relwidth=0.08, relheight=0.08)

        self.name_entry = Entry(self.frame1)
        self.name_entry.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.08)

        # Cellphone
        self.lb_phone = Label(self.frame1, text='Phone', bg='#6CABFA', font=('Verdana', 8, 'bold'))
        self.lb_phone.place(relx=0.02, rely=0.6, relwidth=0.08, relheight=0.08)

        self.phone_entry = Entry(self.frame1)
        self.phone_entry.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.08)

        # City
        self.lb_city = Label(self.frame1, text='City', bg='#6CABFA', font=('Verdana', 8, 'bold'))
        self.lb_city.place(relx=0.5, rely=0.6, relwidth=0.08, relheight=0.08)

        self.city_entry = Entry(self.frame1)
        self.city_entry.place(relx=0.58, rely=0.6, relwidth=0.32, relheight=0.08)

        # Marital Status
        self.lb_status = Label(self.frame1, text='Marital Status', bg='#6CABFA', font=('Verdana', 8, 'bold'))
        self.lb_status.place(relx=0.02, rely=0.85, relwidth=0.15, relheight=0.08)

        self.status_var = StringVar()
        self.status_options = ('Single', 'Married', 'Divorced', 'Widow(er)')
        self.status_var.set('Single')
        self.opmenu = OptionMenu(self.frame1, self.status_var, *self.status_options)
        self.opmenu.place(relx=0.18, rely=0.82, relwidth=0.15, relheight=0.15)

        # Age
        self.lb_age = Label(self.frame1, text='Age', bg='#6CABFA', font=('Verdana', 8, 'bold'))
        self.lb_age.place(relx=0.5, rely=0.85, relwidth=0.08, relheight=0.08)

        self.age_entry = Entry(self.frame1)
        self.age_entry.place(relx=0.58, rely=0.85, relwidth=0.1, relheight=0.08)

        # Clear
        self.bt_clear = Button(self.frame1, text='Clear', bg='#AD7E28', fg='white', activebackground='#FAC76B', activeforeground='white', font=('Verdana', 9, 'bold'), command=self.clear)
        self.bt_clear.place(relx=0.2, rely=0.08, relheight=0.13, relwidth=0.1)

        # Search
        self.bt_search = Button(self.frame1, text='Search', bg='#AD7E28', fg='white', activebackground='#FAC76B', activeforeground='white', font=('Verdana', 9, 'bold'), command=self.search_client)
        self.bt_search.place(relx=0.3, rely=0.08, relheight=0.13, relwidth=0.1)

        # Create
        self.bt_search = Button(self.frame1, text='Create', bg='#AD7E28', fg='white', activebackground='#FAC76B', activeforeground='white', font=('Verdana', 9, 'bold'), command=self.new_client)
        self.bt_search.place(relx=0.6, rely=0.08, relheight=0.13, relwidth=0.1)

        # Update
        self.bt_search = Button(self.frame1, text='Update', bg='#AD7E28', fg='white', activebackground='#FAC76B', activeforeground='white', font=('Verdana', 9, 'bold'), command=self.update_client)
        self.bt_search.place(relx=0.7, rely=0.08, relheight=0.13, relwidth=0.1)

        # Delete
        self.bt_search = Button(self.frame1, text='Delete', bg='#AD7E28', fg='white', activebackground='#FAC76B', activeforeground='white', font=('Verdana', 9, 'bold'), command=self.delete_client)
        self.bt_search.place(relx=0.8, rely=0.08, relheight=0.13, relwidth=0.1)


    def treeview(self):
        self.tree = ttk.Treeview(self.frame2, height=3, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6'))
        self.tree.heading('#0', text='')
        self.tree.heading('#1', text='Number')
        self.tree.heading('#2', text='Name')
        self.tree.heading('#3', text='Phone')
        self.tree.heading('#4', text='City')
        self.tree.heading('#5', text='Status')
        self.tree.heading('#6', text='Age')

        self.tree.column('#0', width=1, stretch=NO)
        self.tree.column('#1', width=50)
        self.tree.column('#2', width=200)
        self.tree.column('#3', width=100)
        self.tree.column('#4', width=100)
        self.tree.column('#5', width=100)
        self.tree.column('#6', width=50)
        
        self.tree.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        self.tree.bind('<Double-1>', self.double_click)

        self.scroll = Scrollbar(self.frame2, orient=VERTICAL, command=self.tree.yview)
        self.tree.config(yscrollcommand=self.scroll.set)
        self.scroll.place(relx=0.96, rely=0.02, relwidth=0.02, relheight=0.96)

Application()