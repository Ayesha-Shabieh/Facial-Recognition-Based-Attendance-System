from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
import os
import csv

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x700+0+0")
        self.root.title("Face Recognition System")

        # text variables
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # top left image
        img = Image.open(r" ")      # add complete path to image
        img = img.resize((457, 150), Image.Resampling.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=457,height=150)

        # top middle image
        img1 = Image.open(r" ")     # add complete path to image
        img1 = img1.resize((455, 150), Image.Resampling.BILINEAR)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        second_label = Label(self.root, image=self.photoimg1)
        second_label.place(x=457, y=0, width=455, height=150)

        # top right image
        img2 = Image.open(r" ")        # add complete path to image
        img2 = img2.resize((455, 150), Image.Resampling.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        third_label = Label(self.root, image=self.photoimg2)
        third_label.place(x=912, y=0, width=455, height=150)

        # background
        img3 = Image.open(r" ")     # add path to complete image
        img3 = img3.resize((1367, 555), Image.Resampling.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_label = Label(self.root, image=self.photoimg3)
        bg_label.place(x=0, y=150, width=1367, height=555)

        title_label = Label(bg_label,text="ATTENDANCE",font=("Times New Roman",35,"bold"),bg="white",fg= "#0A1172")
        title_label.place(x=0, y=0, width=1366, height=45)

        main_frame = Frame(bg_label, bd=2, bg="white") # copy
        main_frame.place(x=10, y=55, width=1346, height=485)

        # left label frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details",
                                font=("Lucida Sans", 12, "bold"), bg="white")
        left_frame.place(x=10, y=10, width=615, height=465)


        # stu id
        id_label = Label(left_frame, text="Student ID", font=("Aptos Display", 12, "bold"), bg="white")
        id_label.grid(row=0, column=0, padx=5, pady=10, sticky=W)
        id_entry = ttk.Entry(left_frame,textvariable=self.var_atten_id,  font=("Calibri", 12, "bold"), width=18)
        id_entry.grid(row=0, column=1, padx=5, pady=10, sticky=W)
        # reg No.
        reg_label = Label(left_frame, text="Registration No.", font=("Aptos Display", 12, "bold"), bg="white")
        reg_label.grid(row=0, column=2, padx=5, pady=10, sticky=W)
        reg_entry = ttk.Entry(left_frame,textvariable=self.var_atten_roll, font=("Calibri", 12, "bold"), width=18)
        reg_entry.grid(row=0, column=3, padx=5, pady=10, sticky=W)
        # name
        name_label = Label(left_frame, text="Name", font=("Aptos Display", 12, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=5, pady=10, sticky=W)
        name_entry = ttk.Entry(left_frame,textvariable=self.var_atten_name, font=("Calibri", 12, "bold"), width=18)
        name_entry.grid(row=1, column=1, padx=5, pady=10, sticky=W)
        # dept
        dep_label = Label(left_frame, text="Department", font=("Aptos Display", 12, "bold"), bg="white")
        dep_label.grid(row=1, column=2, padx=5, pady=10, sticky=W)
        dep_entry = ttk.Entry(left_frame,textvariable=self.var_atten_dep, font=("Calibri", 12, "bold"), width=18)
        dep_entry.grid(row=1, column=3, padx=5, pady=10, sticky=W)
        # time
        time_label = Label(left_frame, text="Time", font=("Aptos Display", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=5, pady=10, sticky=W)
        time_entry = ttk.Entry(left_frame,textvariable=self.var_atten_time, font=("Calibri", 12, "bold"), width=18)
        time_entry.grid(row=2, column=1, padx=5, pady=10, sticky=W)
        # date
        date_label = Label(left_frame, text="Date", font=("Aptos Display", 12, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=5, pady=10, sticky=W)
        date_entry = ttk.Entry(left_frame,textvariable=self.var_atten_date, font=("Calibri", 12, "bold"), width=18)
        date_entry.grid(row=2, column=3, padx=5, pady=10, sticky=W)
        # attendance
        attendance_label = Label(left_frame, text="Attendance", font=("Aptos Display", 12, "bold"), bg="white")
        attendance_label.grid(row=3, column=0, padx=5, pady=10, sticky=W)
        attendance_entry = ttk.Entry(left_frame,textvariable=self.var_atten_attendance, font=("Calibri", 12, "bold"), width=18)
        attendance_entry.grid(row=3, column=1, padx=5, pady=10, sticky=W)

        # buttons frame
        button_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, bg="white")
        button_frame.place(x=15, y=220, width=558, height=36)

        import_b = Button(button_frame,command=self.importCsv,  text="Import csv", font=("Calibri", 12, "bold"), bg="#0A1172",fg="white", width=22)
        import_b.grid(row=0, column=0)

        export_b = Button(button_frame,command=self.exportCsv, text="Export csv", font=("Calibri", 12, "bold"), bg="#0A1172", fg="white", width=22)
        export_b.grid(row=0, column=1)

        reset_b = Button(button_frame,command=self.reset_data,  text="Reset", font=("Calibri", 12, "bold"),bg="#0A1172", fg="white", width=22)
        reset_b.grid(row=0, column=2)

        # right label frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Record",font=("Lucida Sans", 12, "bold"), bg="white")
        right_frame.place(x=635, y=10, width=701, height=465)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=10, width=680, height=420)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.att_table = ttk.Treeview( table_frame,columns=("id","reg", "name","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.att_table.xview)
        scroll_y.config(command=self.att_table.yview)

        self.att_table.heading("id", text="Student ID")
        self.att_table.heading("name", text="Student Name")
        self.att_table.heading("reg", text="Reg no.")
        self.att_table.heading("dep", text="Department")
        self.att_table.heading("time", text="Time")
        self.att_table.heading("date", text="Date")
        self.att_table.heading("attendance", text="Attendance")
        self.att_table["show"] = "headings"

        self.att_table.column("id", width=100)
        self.att_table.column("name", width=100)
        self.att_table.column("reg", width=100)
        self.att_table.column("dep", width=100)
        self.att_table.column("time", width=100)
        self.att_table.column("date", width=100)
        self.att_table.column("attendance", width=100)

        self.att_table.pack(fill=BOTH, expand=1)
        self.att_table.bind("<ButtonRelease>", self.get_cursor)

    def fetchData(self,
                  rows):  # this fn works as it will delete the data which is first in table then insert data into table from csv file
        self.att_table.delete(*self.att_table.get_children())
        for i in rows:
            self.att_table.insert("", END, values=i)

    # import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open csv",
                                         filetypes=(("CSV File", "*.csv"), ("ALl File", "*.*")), parent=self.root)
        # current working directory
        with open(fln) as myfile:  # to read csv file
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)  # csv file sy data ly kr mydata mein append kr diya
            self.fetchData(mydata)  # is data ko table me show krwany k liye (command b button ki deni)

    # export csv
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open csv",
                                               filetypes=(("CSV File", "*.csv"), ("ALl File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)  # in csv
                messagebox.showinfo("Data exported successfully")

        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # get cursor
    def get_cursor(self, event=""):
        cursor_row = self.att_table.focus()
        content = self.att_table.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

        # reset
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()