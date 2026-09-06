from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Help_desk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x700+0+0")
        self.root.title("Face Recognition System")

        # HEADING
        title_label = Label(self.root, text="HELP DESK", font=("Times New Roman", 35, "bold"), bg="white", fg="#0A1172")
        title_label.place(x=0, y=0, width=1366, height=50)

        # TOP IMAGE2
        img2 = Image.open(r" ")     # add complete path to image
        img2 = img2.resize((1366, 655), Image.Resampling.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root, image=self.photoimg2)
        first_label.place(x=0, y=50, width=1366, height=655)

        help_label = Label(self.root, text="{your_email}", font=("Aptos Display", 25, "bold"),
                           bg="navyblue", fg="white")
        help_label.place(x=60, y=300)

        help_label1 = Label(self.root, text="b{your_email}", font=("Aptos Display", 25, "bold"),
                            bg="navyblue", fg="white")
        help_label1.place(x=60, y=350)


if __name__ == "__main__":
    root = Tk()
    obj = Help_desk(root)
    root.mainloop()
