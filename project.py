import tkinter.messagebox
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from b1_student import Student
from b2_traindata import Train
from b3_face_detection import Face
from b5_attendance import Attendance
from b6_developer import Developer
from b7_help import Help_desk
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x700+0+0")
        self.root.title("Face Recognition System")

        # top left image
        img = Image.open(r" ")      # add complete path to image
        img = img.resize((457, 150), Image.Resampling.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=457,height=150)
        # first_label.pack(fill="both", expand=True)
        # first_label.grid(row=0, column=0)

        # top middle image
        img1 = Image.open(r" ")      # add complete path to image
        img1 = img1.resize((455, 150), Image.Resampling.BILINEAR)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        second_label = Label(self.root, image=self.photoimg1)
        second_label.place(x=457, y=0, width=455, height=150)
        # second_label.pack(fill="both", expand=True)
        # second_label.grid(row=0, column=1)

        # top right image
        img2 = Image.open(r" ")      # add complete path to image
        img2 = img2.resize((455, 150), Image.Resampling.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        third_label = Label(self.root, image=self.photoimg2)
        third_label.place(x=912, y=0, width=455, height=150)

        # background
        img3 = Image.open(r" ")        # add complete path to image
        img3 = img3.resize((1367, 555), Image.Resampling.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_label = Label(self.root, image=self.photoimg3)
        bg_label.place(x=0, y=150, width=1367, height=555)

        title_label = Label(bg_label,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("Times New Roman",35,"bold"),bg="white",fg= "#0A1172")
        title_label.place(x=0, y=0, width=1366, height=45)

        # student details button
        b_1 = Button(bg_label,text = "Student Info",command=self.student_details ,cursor = "hand2",font=("Times New Roman",20,"bold"),bg="white",fg= "#0A1172" )
        b_1.place(x=168, y=185, width=220, height=75)

        # face detect button
        b_2 = Button(bg_label,command=self.face, text="Face Detection", cursor="hand2", font=("Times New Roman", 20, "bold"), bg="white",fg="#0A1172")
        b_2.place(x=438, y=185, width=220, height=75)

        # attendance button
        b_1 = Button(bg_label,command=self.attendance, text="Attendance", cursor="hand2", font=("Times New Roman", 20, "bold"), bg="white", fg="#0A1172")
        b_1.place(x=708, y=185, width=220, height=75)

        # help button
        b_2 = Button(bg_label,command=self.help, text="Help", cursor="hand2", font=("Times New Roman", 20, "bold"), bg="white",fg="#0A1172")
        b_2.place(x=978, y=185, width=220, height=75)

        # train data button
        b_1 = Button(bg_label,command=self.train_data, text="Train Data", cursor="hand2", font=("Times New Roman", 20, "bold"), bg="white", fg="#0A1172")
        b_1.place(x=168, y=335, width=220, height=75)

        # photos button
        b_2 = Button(bg_label,command=self.open_img, text="Photos", cursor="hand2", font=("Times New Roman", 20, "bold"), bg="white", fg="#0A1172")
        b_2.place(x=438, y=335, width=220, height=75)

        # developer button
        b_1 = Button(bg_label,command=self.developer, text="Developer", cursor="hand2", font=("Times New Roman", 20, "bold"), bg="white", fg="#0A1172")
        b_1.place(x=708, y=335, width=220, height=75)

        # exit button
        b_2 = Button(bg_label, command=self.iexit , text="Exit", cursor="hand2", font=("Times New Roman", 20, "bold"), bg="white", fg="#0A1172")
        b_2.place(x=978, y=335, width=220, height=75)

    def open_img(self):
        os.startfile(r" ")         # add complete path to image


    # FUNCTION BUTTONS......
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face(self):
        self.new_window = Toplevel(self.root)
        self.app = Face(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help(self):
        self.new_window = Toplevel(self.root)
        self.app = Help_desk(self.new_window)

    def iexit(self):
        self.iexit = tkinter.messagebox.askyesno("Face Recognition System","Are you sure you want to exit?",parent=self.root)
        if self.iexit > 0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()


