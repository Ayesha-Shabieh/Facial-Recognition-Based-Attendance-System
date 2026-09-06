from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x700+0+0")
        self.root.title("Face Recognition System")

        # variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_reg=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_teacher=StringVar()

        # top left image
        img = Image.open(r" ")      # add complete path to image
        img = img.resize((457, 150), Image.Resampling.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=457, height=150)

        # top middle image
        img1 = Image.open(r" ")       # add complete path to image
        img1 = img1.resize((455, 150), Image.Resampling.BILINEAR)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        second_label = Label(self.root, image=self.photoimg1)
        second_label.place(x=457, y=0, width=455, height=150)

        # top right image
        img2 = Image.open(r" ")         # add complete path to image
        img2 = img2.resize((455, 150), Image.Resampling.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        third_label = Label(self.root, image=self.photoimg2)
        third_label.place(x=912, y=0, width=455, height=150)

        # background
        img3 = Image.open(r" ")       # add complete path to image
        img3 = img3.resize((1367, 555), Image.Resampling.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_label = Label(self.root, image=self.photoimg3)
        bg_label.place(x=0, y=150, width=1367, height=555)

        title_label = Label(bg_label, text="STUDENT INFORMATION", font=("Times New Roman", 35, "bold"), bg="white", fg="#0A1172")
        title_label.place(x=0, y=0, width=1366, height=45)

        main_frame = Frame(bg_label,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1346,height=490)

        # left label frame
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Lucida Sans", 12, "bold"),bg="white")
        left_frame.place(x=10,y=10,width=615,height=470)

        # current course
        current_course_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Current Course",font=("Lucida Sans", 12, "bold"), bg="white")
        current_course_frame.place(x=20, y=40, width=595, height=135)

        # Department
        dept_label = Label(current_course_frame,text="Department",font=("Aptos Display", 12, "bold"),bg="white")
        dept_label.grid (row=0,column=0,padx=10,sticky=W)
        dept_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("Calibri", 12, "bold"),width=18,state="readonly")
        dept_combo["values"]=("Select Department","Computer Science","Computer Engineering","Civil Engineering","Architecture",
                              "Electrical Engineering","Mechanical Engineering","Mathematics","Mechatronics","Physics","Humanities")
        dept_combo.current(0)
        dept_combo.grid (row=0,column=1,padx=2,pady=10)
        # course
        course_label = Label(current_course_frame, text="Course", font=("Aptos Display", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_entry = ttk.Entry(current_course_frame,textvariable=self.var_course, font=("Calibri", 12, "bold"), width=20)
        course_entry.grid(row=0, column=3, padx=2, pady=10, sticky=W)
        # year
        year_label = Label(current_course_frame, text="Year", font=("Aptos Display", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("Calibri", 12, "bold"), width=18, state="readonly")
        year_combo["values"] = ("Select Year", "2020","2021","2022","2023","2024")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10)
        # semester
        semester_label = Label(current_course_frame, text="Semester", font=("Aptos Display", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("Calibri", 12, "bold"), width=18, state="readonly")
        semester_combo["values"] = ("Select Semester", "I","II","III","IV","V","VI","VII","VIII",)
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10)

        # class student information
        cl_stu_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Class Student Information",font=("Lucida Sans", 12, "bold"), bg="white")
        cl_stu_frame.place(x=20, y=185, width=595, height=285)
        # Student ID
        stu_id_label = Label(cl_stu_frame, text="Student ID", font=("Aptos Display", 12, "bold"), bg="white")
        stu_id_label.grid(row=0, column=0, padx=2,pady=5, sticky=W)
        stu_id_entry = ttk.Entry(cl_stu_frame,textvariable=self.var_std_id, font=("Calibri", 12, "bold"), width=18)
        stu_id_entry.grid(row=0, column=1, padx=2,pady=5, sticky=W)
        # Student Name
        stu_name_label = Label(cl_stu_frame, text="Student Name", font=("Aptos Display", 12, "bold"), bg="white")
        stu_name_label.grid(row=0, column=2, padx=2, pady=5, sticky=W)
        stu_name_entry = ttk.Entry(cl_stu_frame,textvariable=self.var_std_name, font=("Calibri", 12, "bold"), width=18)
        stu_name_entry.grid(row=0, column=3, padx=2, pady=5, sticky=W)
        # not writing clss division.. what's it for??
        # Registration No.
        reg_label = Label(cl_stu_frame, text="Registration No.", font=("Aptos Display", 12, "bold"), bg="white")
        reg_label.grid(row=1, column=0, padx=2, pady=5, sticky=W)
        reg_entry = ttk.Entry(cl_stu_frame,textvariable=self.var_reg, font=("Calibri", 12, "bold"), width=18)
        reg_entry.grid(row=1, column=1, padx=2, pady=5, sticky=W)
        # Gender
        gen_label = Label(cl_stu_frame, text="Gender", font=("Aptos Display", 12, "bold"), bg="white")
        gen_label.grid(row=1, column=2, padx=2, pady=5, sticky=W)
        gen_combo = ttk.Combobox(cl_stu_frame, textvariable=self.var_gender,
                                      font=("Calibri", 12, "bold"), width=16, state="readonly")
        gen_combo["values"] = ("Male","Female")
        gen_combo.current(0)
        gen_combo.grid(row=1, column=3, padx=2, pady=5, sticky=W)

        # dob
        dob_label = Label(cl_stu_frame, text="Date of Birth", font=("Aptos Display", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=0, padx=2, pady=5, sticky=W)
        dob_entry = ttk.Entry(cl_stu_frame,textvariable=self.var_dob, font=("Calibri", 12, "bold"), width=18)
        dob_entry.grid(row=2, column=1, padx=2, pady=5, sticky=W)
        # Phone No.
        num_label = Label(cl_stu_frame, text="Phone No.", font=("Aptos Display", 12, "bold"), bg="white")
        num_label.grid(row=2, column=2, padx=2, pady=5, sticky=W)
        num_entry = ttk.Entry(cl_stu_frame,textvariable=self.var_phone, font=("Calibri", 12, "bold"), width=18)
        num_entry.grid(row=2, column=3, padx=2, pady=5, sticky=W)
        # email
        email_label = Label(cl_stu_frame, text="Email Adress", font=("Aptos Display", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=2, pady=5, sticky=W)
        email_entry = ttk.Entry(cl_stu_frame,textvariable=self.var_email, font=("Calibri", 12, "bold"), width=18)
        email_entry.grid(row=3, column=1, padx=2, pady=5, sticky=W)
        # teacher
        teacher_label = Label(cl_stu_frame, text="Teacher Name", font=("Aptos Display", 12, "bold"), bg="white")
        teacher_label.grid(row=3, column=2, padx=2, pady=5, sticky=W)
        teacher_entry = ttk.Entry(cl_stu_frame,textvariable=self.var_teacher, font=("Calibri", 12, "bold"), width=18)
        teacher_entry.grid(row=3, column=3, padx=2, pady=5, sticky=W)

        # radio buttons
        self.var_radio1=StringVar()
        radio_b1 = ttk.Radiobutton(cl_stu_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radio_b1.grid(row=4, column=0)

        radio_b2 = ttk.Radiobutton(cl_stu_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radio_b2.grid(row=4, column=1)

        # buttons frame
        button_frame = LabelFrame(cl_stu_frame, bd=2, relief=RIDGE,bg="white")
        button_frame.place(x=15, y=180, width=558, height=36)

        save_b=Button(button_frame,command=self.add_data,text="Save",font=("Calibri", 12, "bold"),bg="#0A1172",fg="white",width=16)
        save_b.grid(row=0,column=0)

        update_b=Button(button_frame,command=self.update_data,text="Update",font=("Calibri", 12, "bold"),bg="#0A1172",fg="white",width=16)
        update_b.grid(row=0,column=1)

        delete_b=Button(button_frame,command=self.delete_data,text="Delete",font=("Calibri", 12, "bold"),bg="#0A1172",fg="white",width=16)
        delete_b.grid(row=0,column=2)

        reset_b=Button(button_frame,command=self.reset_data,text="Reset",font=("Calibri", 12, "bold"),bg="#0A1172",fg="white",width=16)
        reset_b.grid(row=0,column=3)

        button_frame1 = LabelFrame(cl_stu_frame, bd=2, relief=RIDGE, bg="white")
        button_frame1.place(x=15, y=216, width=557, height=36)

        take_photo_b = Button(button_frame1,command=self.generate_dataset, text="Take Photo sample", font=("Calibri", 12, "bold"), bg="#0A1172", fg="white",width=68)
        take_photo_b.grid(row=0, column=0)

        # right label frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Record",font=("Lucida Sans", 12, "bold"), bg="white")
        right_frame.place(x=635, y=10, width=701, height=470)

        # Table Frame..................
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=10, width=680, height=425)
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.stu_table=ttk.Treeview(table_frame,columns=("dep", "course", "year", "sem", "id", "name","reg","gender",  "dob", "email", "phone","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.stu_table.xview)
        scroll_y.config(command=self.stu_table.yview)

        self.stu_table.heading("dep", text="Department")
        self.stu_table.heading("course", text="Course")
        self.stu_table.heading("year", text="Year")
        self.stu_table.heading("sem", text="Semester")
        self.stu_table.heading("id", text="Student ID")
        self.stu_table.heading("name", text="Student Name")
        self.stu_table.heading("reg", text="Reg no.")
        self.stu_table.heading("gender", text="Gender")
        self.stu_table.heading("dob", text="Date of Birth")
        self.stu_table.heading("email", text="Email Address")
        self.stu_table.heading("phone", text="Phone no.")
        self.stu_table.heading("teacher", text="Teacher Name")
        self.stu_table.heading("photo", text="Photo Sample")
        self.stu_table["show"] = "headings"

        self.stu_table.column("dep", width=100)
        self.stu_table.column("course", width=100)
        self.stu_table.column("year", width=100)
        self.stu_table.column("sem", width=100)
        self.stu_table.column("id", width=100)
        self.stu_table.column("name", width=100)
        self.stu_table.column("reg", width=100)
        self.stu_table.column("gender", width=100)
        self.stu_table.column("dob", width=100)
        self.stu_table.column("email", width=100)
        self.stu_table.column("phone", width=100)
        self.stu_table.column("teacher", width=100)
        self.stu_table.column("photo", width=100)

        self.stu_table.pack(fill=BOTH,expand=1)
        self.stu_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # function to add data
    def add_data(self): #button mein command dein gy
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("ERROR","All fields are required",parent=self.root)
        else: #impport mysql
            try:
                conn=mysql.connector.connect(host="localhost",username={"your user name"},password={"your mysql database password"},database={"name of database you created for this project"})
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_dep.get(),
                                                                                       self.var_course.get(),
                                                                                       self.var_year.get(),
                                                                                       self.var_semester.get(),
                                                                                       self.var_std_id.get(),
                                                                                       self.var_std_name.get(),
                                                                                       self.var_reg.get(),
                                                                                       self.var_gender.get(),
                                                                                       self.var_dob.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_phone.get(),
                                                                                       self.var_teacher.get(),
                                                                                       self.var_radio1.get()
                                                                                                                  ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details have been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # fetch_data..............
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username={"your user name"},password={"your mysql database password"},database={"name of database you created for this project"})
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.stu_table.delete(*self.stu_table.get_children())
            for i in data:
                self.stu_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # get cursor.........
    def get_cursor(self, event=""):
        cursor_focus = self.stu_table.focus()
        content = self.stu_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_reg.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_teacher.set(data[11]),
        self.var_radio1.set(data[12])

    # update data.............................
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("ERROR", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if update > 0:
                    conn=mysql.connector.connect(host="localhost",username={"your user name"},password={"your mysql database password"},database={"name of database you created for this project"})
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Gender=%s,Dob=%s,Reg_no =%s,Email=%s,Phone=%s,Teacher=%s,Photosample=%s where student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_reg.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()

                        ))
                    messagebox.showinfo("Success", "Student details have been updated successfully", parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()

                else:
                    if not update:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # del.............
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id is must required")
        else:
            try:
                delete=messagebox.askyesno("Delete student info","Do you want to delete this student?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username={"your user name"},password={"your mysql database password"},database={"name of database you created for this project"})
                    my_cursor = conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student details deleted successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # reset.............
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set(""),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_reg.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    # generate data set, take photo sample
    def generate_dataset(self):
        if self.var_dep.get() == "Select department" or self.var_std_name.get() == "" or self.var_std_id.get() == " ":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username={"your user name"},password={"your mysql database password"},database={"name of database you created for this project"})
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute(    "update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Gender=%s,Dob=%s,Reg_no =%s,Email=%s,Phone=%s,Teacher=%s,Photosample=%s where student_id=%s",
                (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_reg.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = r"add_your_own_file_path" + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed successfully!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)





if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

