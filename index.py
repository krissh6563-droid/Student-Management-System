from tkinter import *
from tkinter import ttk
import pymysql


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Student Management System",
                      bd=10, relief=GROOVE, font=("times new roman", 40, "bold"))
        title.pack(side=TOP, fill=X)

        # All variables
        self.roll_no_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        # frame 1
        frame1 = Frame(self.root, bd=4, relief=RIDGE,)
        frame1.place(x=20, y=100, width=450, height=580)

        # Manage Student
        m_title = Label(frame1, text="Manage Student",
                        font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        # lable for Roll no.
        lbl_roll = Label(frame1, text="Roll No.",
                         font=("times new roman", 15, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_roll = Entry(frame1, font=("times new roman", 15,
                                       "bold"), textvariable=self.roll_no_var)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        # lable for Name
        lbl_name = Label(frame1, text="Name", font=(
            "times new roman", 15, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(frame1, font=("times new roman", 15,
                                       "bold"), textvariable=self.name_var)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        # labke for email
        lbl_email = Label(frame1, text="E-mail",
                          font=("times new roman", 15, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_email = Entry(frame1, font=("times new roman", 15,
                                        "bold"), textvariable=self.email_var)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        # lable for gender
        lbl_gender = Label(frame1, text="Gender", font=(
            "times new roman", 15, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        combo_gender = ttk.Combobox(frame1, font=(
            "times new roman", 14, "bold"), state="readonly", textvariable=self.gender_var)
        combo_gender['values'] = ("Male", "Female", "Others")
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        # lable for contact
        lbl_contact = Label(frame1, text="Contact",
                            font=("times new roman", 15, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_contact = Entry(frame1, font=(
            "times new roman", 15, "bold"), textvariable=self.contact_var)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        # lable for DOB
        lbl_dob = Label(frame1, text="DOB", font=(
            "times new roman", 15, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_dob = Entry(frame1, font=("times new roman", 15,
                                      "bold"), textvariable=self.dob_var)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # lable for address
        lbl_address = Label(frame1, text="Address",
                            font=("times new roman", 15, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.txt_address = Text(frame1, width=25, height=4, font=("", 10))
        self.txt_address.grid(row=7, column=1, pady=10, padx=20)

        # button frame
        btn_frame = Frame(frame1, bd=4, relief=RIDGE)
        btn_frame.place(x=20, y=480, width=320, height=50)

        # buttons for frame
        add_btn = Button(btn_frame, text="ADD", width=5,
                         command=self.add_student)
        add_btn.grid(row=0, column=0, pady=5, padx=5)

        delete_btn = Button(btn_frame, text="DELETE", width=5,command=self.delete_data)
        delete_btn.grid(row=0, column=1, pady=5, padx=5)

        update_btn = Button(btn_frame, text="UPDATE",
                            width=5, command=self.update_data)
        update_btn.grid(row=0, column=2, pady=5, padx=5)

        clear_btn = Button(btn_frame, text="CLEAR",
                           width=5, command=self.clear)
        clear_btn.grid(row=0, column=3, pady=5, padx=5)

        # detail frame
        frame2 = Frame(self.root, bd=4, relief=RIDGE)
        frame2.place(x=500, y=100, width=780, height=580)

        lbl_search = Label(frame2, text="Search By",
                           font=("times new roman", 15, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        combo_search = ttk.Combobox(frame2, font=(
            "times new roman", 14, "bold"), state="readonly", width=10)
        combo_search['values'] = ("Name", "Roll No.", "Contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_search = Entry(frame2, font=("times new roman", 15, "bold"))
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        search_btn = Button(frame2, text="SEARCH", width=7)
        search_btn.grid(row=0, column=3, pady=5, padx=5)

        show_btn = Button(frame2, text="SHOW ALL", width=10)
        show_btn.grid(row=0, column=4, pady=5, padx=5)

        # table frame
        table_frame = Frame(frame2, bd=4, relief=RIDGE)
        table_frame.place(x=7, y=70, width=760, height=495)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.students_table = ttk.Treeview(table_frame, columns=(
            "Roll No.", "Name", "E-mail", "Gender", "Contact", "DOB", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.students_table.xview)
        scroll_y.config(command=self.students_table.yview)
        self.students_table.heading("Roll No.", text="Roll No.")
        self.students_table.heading("Name", text="Name")
        self.students_table.heading("E-mail", text="E-mail")
        self.students_table.heading("Gender", text="Gender")
        self.students_table.heading("Contact", text="Contact")
        self.students_table.heading("DOB", text="DOB")
        self.students_table.heading("Address", text="Address")
        self.students_table['show'] = 'headings'
        self.students_table.column("Roll No.", width=70)
        self.students_table.column("Name", width=150)
        self.students_table.column("Gender", width=80)
        self.students_table.column("Contact", width=150)
        self.students_table.column("DOB", width=100)
        self.students_table.pack(fill=BOTH, expand=1)
        self.students_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    def add_student(self):
        connection = pymysql.connect(
            host="localhost", user="root", password="Aditya2000@@", database="stm")
        cur = connection.cursor()
        cur.execute("INSERT INTO student_table VALUES(%s,%s,%s,%s,%s,%s,%s)", (
            self.roll_no_var.get(),
            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.dob_var.get(),
            self.txt_address.get('1.0', END)

        ))
        connection.commit()
        self.fetch_data()
        self.clear()
        connection.close()

    def fetch_data(self):
        connection = pymysql.connect(
            host="localhost", user="root", password="Aditya2000@@", database="stm")
        cur = connection.cursor()
        cur.execute("select * from student_table")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.students_table.delete(*self.students_table.get_children())
            for row in rows:
                self.students_table.insert('', END, values=row)
            connection.commit()
        connection.close()

    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0", END)

    def get_cursor(self, ev):
        cursor_row = self.students_table.focus()
        contents = self.students_table.item(cursor_row)
        row = contents['values']
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[6])

    def update_data(self):
        connection = pymysql.connect(
            host="localhost", user="root", password="Aditya2000@@", database="stm")
        cur = connection.cursor()
        cur.execute("UPDATE student_table SET name = %s,email=%s,gender=%s,contact=%s,dob=%s,address=%s,WHERE roll_no=%s", (

            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.dob_var.get(),
            self.txt_address.get('1.0', END),
            self.roll_no_var.get()


        ))
        connection.commit()
        self.fetch_data()
        self.clear()
        connection.close()
    def delete_data(self):
        connection = pymysql.connect(
            host="localhost", user="root", password="Aditya2000@@", database="stm")
        cur = connection.cursor()
        cur.execute("delete  from student_table where roll_no=%s",self.roll_no_var.get())
        connection.commit()
        connection.close()
        self.fetch_data()
        self.clear()



root = Tk()
obj = Student(root)
root.mainloop()
