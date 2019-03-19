from tkinter import *
from signal_canvas import SignalCanvas
from signal_shifter import SignalShifter
from constants import *

# signal = [0 for _ in range(canvas_width)]
# signals = [None for _ in range(canvas_width)]

# state = None


# from PIL import Image, ImageTk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def callback(self):
        self.ssh.signal1 = self.c1.signal
        self.ssh.signal2 = self.c1.signal
        print("applied")
        # self.ssh.create_canvas(self.master)

    def initUI(self):
        # self.master.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame", background="#333")
        self.c1 = SignalCanvas("blue")
        self.c1.create_canvas(self.master)
        self.c2 = SignalCanvas("red")
        self.c2.create_canvas(self.master)
        self.ssh = SignalShifter("red", self.c1.signal, self.c2.signal)
        self.master.title("Jot of Convolution")

        b = Button(self.master, text="APPLY", command=self.callback)
        message = Label(self.master, text="Draw your Signal")
        message.pack(side=BOTTOM)

        self.c1.w.place(x=0, y=0)
        self.c2.w.place(x=canvas_width, y=0)
        self.ssh.create_canvas(master=self.master)
        self.ssh.w.place(x=0, y=canvas_height)
        b.pack()


def main():
    root = Tk()
    root.geometry("300x280+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
#
# master = Tk()
#
# mainloop()
