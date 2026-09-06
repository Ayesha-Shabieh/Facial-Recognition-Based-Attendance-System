from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x700+0+0")
        self.root.title("Face Recognition System")

        # HEADING
        title_label = Label(self.root, text="DEVELOPERS", font=("Times New Roman", 35, "bold"), bg="white",
                            fg="#0A1172")
        title_label.place(x=0, y=0, width=1366, height=50)
        # TOP IMAGE
        img = Image.open(r" ")      # add complete path to image
        img = img.resize((650, 655), Image.Resampling.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=716, y=50, width=650, height=655)

        img1 = Image.open(r" ")     # add complete path to image
        img1 = img1.resize((717, 655), Image.Resampling.BILINEAR)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=0, y=50, width=717, height=655)

        # INFO
        dev_label = Label(self.root, text="Shabieh Batool and Ayesha Ahmad developed an advanced attendance ",
                          font=("Aptos Display", 15, "bold"), bg="skyblue", fg="black")
        dev_label.place(x=7, y=100)

        dev_label1 = Label(self.root, text="system centered around facial recognition technology. Their project",
                           font=("Aptos Display", 15, "bold"), bg="skyblue", fg="black")
        dev_label1.place(x=7, y=150)

        dev_label1 = Label(self.root, text="involved implementing a complex face recognition algorithm, utilizing",
                           font=("Aptos Display", 15, "bold"), bg="skyblue", fg="black")
        dev_label1.place(x=7, y=200)

        dev_label1 = Label(self.root, text="machine learning to create a system capable of swiftly and accurately",
                           font=("Aptos Display", 15, "bold"), bg="skyblue", fg="black")
        dev_label1.place(x=7, y=250)

        dev_label1 = Label(self.root, text="identifying individuals in real-time. Their goal was to simplify the     ",
                           font=("Aptos Display", 15, "bold"), bg="skyblue", fg="black")
        dev_label1.place(x=7, y=300)

        dev_label1 = Label(self.root, text="attendance process by automating it through facial recognition,    ",
                           font=("Aptos Display", 15, "bold"), bg="skyblue", fg="black")
        dev_label1.place(x=7, y=350)

        dev_label1 = Label(self.root, text="replacing the need for manual attendance-taking with a more        ",
                           font=("Aptos Display", 15, "bold"), bg="skyblue", fg="black")
        dev_label1.place(x=7, y=400)

        dev_label1 = Label(self.root, text="efficient and reliable method.", font=("Aptos Display", 15, "bold"),
                           bg="skyblue", fg="black")
        dev_label1.place(x=7, y=450)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()