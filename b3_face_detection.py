from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x700+0+0")
        self.root.title("Face Recognition System")

        # HEADING
        title_label = Label(self.root, text="FACE DETECTION", font=("Times New Roman", 35, "bold"), bg="white",
                            fg="#0A1172")
        title_label.place(x=0, y=0, width=1366, height=50)

        # TOP IMAGE
        img = Image.open(r" ")      # add complete file path here
        img = img.resize((716, 670), Image.Resampling.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label1 = Label(self.root, image=self.photoimg)
        first_label1.place(x=650, y=50, width=716, height=670)

        img1 = Image.open(r" ")     # add complete file path here
        img1 = img1.resize((650, 670), Image.Resampling.BILINEAR)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=0, y=50, width=650, height=670)

        # BUTTON
        b_1 = Button(first_label1,command=self.face_recog, text="Frontal Face Recognition", cursor="hand2",
                     font=("Times New Roman", 18, "bold"), bg="black", fg="white")
        b_1.place(x=20, y=550, width=300, height=40)

    # attendance

    def mark_attendance(self,i,r,n,d):
        with open ("attendance.csv","r+",newline="\n") as f:
            mydatalist = f.readlines()
            namelist =[]
            for line in mydatalist:
                entry=line.split((","))
                namelist.append(entry[0])
            # f.seek(0)
            if ((i not in namelist) and (r not in namelist) and (n not in namelist) and (d not in namelist)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i[1:-2]},{r[1:-2]},{n[1:-2]},{d[1:-2]},{dtstring},{d1},Present")



        # face recognition
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            coord = []

            for (x, y, w, h) in features:  # we are making rectangle around our face to detect
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn=mysql.connector.connect(host="localhost",username={"your user name"},password={"your mysql database password"},database={"name of database you created for this project"})
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "".join(str(n))

                my_cursor.execute("select Reg_no from student where student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "".join(str(r))

                my_cursor.execute("select Dep from student where student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "".join(str(d))

                my_cursor.execute("select student_id from student where student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "".join(str(i))



                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y - 85), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dept:{d}", (x, y - 60), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Reg_no:{r}", (x, y - 35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    # side of rect, font, font scale,color,thickness
                    cv2.putText(img, f"Name:{n}", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  # for detection
        clf = cv2.face.LBPHFaceRecognizer_create()  # for recognize
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face recognition", img)

            if cv2.waitKey(1) == 13:  # for closing window
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face(root)
    root.mainloop()

