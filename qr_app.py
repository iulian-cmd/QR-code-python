from tkinter import *
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage


class Qr_Generator:

    # Constructor method for the class Qr_Generator
    def __init__(self, root):
        # Creating a frame for the window
        self.root = root
        # Setting the title of the window
        self.root.title("QR Code Generator")
        # Setting the size of the window
        self.root.geometry("900x500+200+50")
        # Setting the background color of the window
        self.root.config(bg="#554971")
        # Setting the resizable property of the window
        self.root.resizable(False, False)

        # title label for the window
        title = Label(self.root, text="QR Code Generator", font=(
            "times new roman", 40), bg="#36213E", fg="#B8F3FF").place(x=0, y=50, relwidth=1)

        # QR Code frame for the window
        qr_frame = Frame(self.root, bd=2, relief=RIDGE, bg="#63768D")

        # Setting the size of the frame for the window
        qr_frame.place(x=50, y=150, width=800, height=300)

        # QR Code label for the window
        qr_label = Label(qr_frame, text="QR Code", font=(
            "times new roman", 15, "bold"), bg="#36213E", fg="#B8F3FF").place(x=0, y=0, relwidth=1)


root = Tk()
obj = Qr_Generator(root)
root.mainloop()
