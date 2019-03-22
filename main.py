from tkinter import *
from signal_canvas import SignalCanvas
from signal_shifter import SignalShifter
from constants import *
from product_canvas import ProductCanvas
from convolution_canvas import *
# signal = [0 for _ in range(canvas_width)]
# signals = [None for _ in range(canvas_width)]

# state = None


# from PIL import Image, ImageTk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style


class Example(Frame):

    def __init__(self):
        super().__init__(width=2 * canvas_width, height=canvas_height * 4)

        self.initUI()

    def callback(self):
        ## TODO : reverse the signal
        temp = self.c1.signal.copy()
        for i in range(len(temp)):
            self.ssh.signal1[i] = temp[len(temp) - i - 1]
        self.ssh.signal2 = self.c2.signal
        self.ssh.plot()
        print("applied")
        # self.ssh.create_canvas(self.master)

    def initUI(self):
        # self.master.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)
        # self.place(relx=.5, rely=.5, anchor="c")
        # self.config()
        # Style().configure("TFrame", background="#333")
        self.master.title("Jot of Convolution")
        self.c1 = SignalCanvas("blue")
        self.c1.create_canvas(self.master)
        self.c2 = SignalCanvas("red")
        self.c2.create_canvas(self.master)
        self.pc = ProductCanvas("red", None)
        self.cc = ConvolutionCanvas("blue",self.pc)
        self.ssh = SignalShifter("blue", self.c1.signal, self.c2.signal, self.pc,self.cc)
        self.pc.shifter = self.ssh
        self.cc.create_canvas(self.master)
        self.pc.create_canvas(self.master)
        b = Button(self.master, text="APPLY", command=self.callback)
        message = Label(self.master, text="Draw your Signal")
        message.pack(side=BOTTOM)

        self.c1.w.place(x=0, y=0)
        self.c2.w.place(x=canvas_width, y=0)
        self.ssh.create_canvas(master=self.master)
        self.ssh.w.place(x=0, y=canvas_height)
        self.pc.w.place(x=0, y=2 * canvas_height)
        self.cc.w.place(x=0, y=3 * canvas_height)
        b.pack()

    # def minsize(self):
    #     return 2 * canvas_width, 3 * canvas_height


def main():
    root = Tk()
    root.geometry("500x550+450+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
#
# master = Tk()
#
# mainloop()
