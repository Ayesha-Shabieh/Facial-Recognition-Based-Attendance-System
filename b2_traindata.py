from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x700+0+0")
        self.root.title("Face Recognition System")


# HEADING
        title_label = Label(self.root, text="TRAIN DATA SET", font=("Times New Roman", 35, "bold"), bg="white", fg="#0A1172")
        title_label.place(x=0, y=0, width=1366, height=45)
# TOP IMAGE
        img = Image.open(r" ")      # add complete file path here
        img = img.resize((1366, 250), Image.Resampling.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=45,width=1366,height=250)
# BUTTON
        b_1 = Button(self.root,command=self.train_classifier,text = "TRAIN DATA" ,cursor = "hand2",font=("Times New Roman",30,"bold"),bg="#0A1172",fg= "white" )
        b_1.place(x=0, y=295, width=1366, height=70)
# BOTTOM IMAGE
        img1 = Image.open(r" ")         # add complete file path here
        img1 = img1.resize((1366, 340), Image.Resampling.BILINEAR)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(self.root,image=self.photoimg1)
        first_label.place(x=0,y=365,width=1366,height=340)


    def train_classifier(self):
        data_dir = (r" ")       # add complete file path here
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")    # grayscale image
            image_np = np.array(img,"uint8")
            id = int(os.path.split(image)[1].split(".")[1])

            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training Images",image_np)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # training the classifier and saving data
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed successfully.")










if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()