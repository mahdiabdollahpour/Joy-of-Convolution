from descrete_mode.signal_canvas_d import SignalCanvas
from descrete_mode.signal_shifter_d import SignalShifter
from descrete_mode.product_canvas_d import ProductCanvas
from descrete_mode.convolution_canvas_d import *
# signal = [0 for _ in range(canvas_width)]
# signals = [None for _ in range(canvas_width)]

# state = None


# from PIL import Image, ImageTk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label

## TODO : add some predefined signals , clear button to clear all, shifter moves suddenly after first click
conv_canvas_height_coef = 1.5


class Example(Frame):

    def __init__(self):
        super().__init__(width=2 * canvas_width, height=canvas_height * 4)

        self.initUI()

    def reset(self):
        self.c1.reset()
        self.c2.reset()
        self.cc.reset()
        self.pc.reset()
        self.ssh.reset()

    def callback(self):
        ## TODO : reverse the signal
        temp = self.c1.signal.copy()
        for i in range(1, len(temp)):
            print(len(temp) - i)
            self.ssh.signal1[i] = temp[len(temp) - i]
        self.ssh.signal2 = self.c2.signal
        self.ssh.plot()
        self.cc.do_all_conv()
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
        self.pc = ProductCanvas(int(large_canvas_width_coef * canvas_width), "red", None)
        self.cc = ConvolutionCanvas(int(large_canvas_width_coef * canvas_width), "red", self.pc,
                                    conv_canvas_height_coef)
        self.ssh = SignalShifter(int(large_canvas_width_coef * canvas_width), self.c1.signal_color,
                                 self.c2.signal_color, self.c1.signal, self.c2.signal,
                                 self.pc, self.cc)
        self.pc.shifter = self.ssh
        self.cc.create_canvas(self.master)
        self.pc.create_canvas(self.master)
        b = Button(self.master, text="Apply", command=self.callback, height=1, width=5)
        step1 = Button(self.master, text="Step", command=self.c1.step, height=1, width=5)

        ramp1 = Button(self.master, text="Ramp", command=self.c1.ramp, height=1, width=5)
        pulse1 = Button(self.master, text="Pulse", command=self.c1.pulse, height=1, width=5)
        step2 = Button(self.master, text="Step", command=self.c2.step, height=1, width=5)
        ramp2 = Button(self.master, text="Ramp", command=self.c2.ramp, height=1, width=5)
        pulse2 = Button(self.master, text="Pulse", command=self.c2.pulse, height=1, width=5)

        reset_b = Button(self.master, text="Reset", command=self.reset, height=1, width=5)

        message = Label(self.master, text="Draw your Signal")
        message.pack(side=BOTTOM)

        self.c1.w.place(x=0, y=0)
        self.c2.w.place(x=(large_canvas_width_coef - 1) * canvas_width, y=0)
        self.ssh.create_canvas(master=self.master)
        self.ssh.w.place(x=0, y=canvas_height)
        self.pc.w.place(x=0, y=2 * canvas_height)
        self.cc.w.place(x=0, y=3 * canvas_height)
        step1.place(x=canvas_width + int(canvas_width / buttons_padding), y=0)
        ramp1.place(x=canvas_width + int(canvas_width / buttons_padding), y=int(canvas_height / 4))
        pulse1.place(x=canvas_width + int(canvas_width / buttons_padding), y=2 * int(canvas_height / 4))

        step2.place(x=canvas_width + int((buttons_padding - 5) * canvas_width / buttons_padding), y=0)
        ramp2.place(x=canvas_width + int((buttons_padding - 5) * canvas_width / buttons_padding),
                    y=int(canvas_height / 4))
        pulse2.place(x=canvas_width + int((buttons_padding - 5) * canvas_width / buttons_padding),
                     y=2 * int(canvas_height / 4))

        reset_b.place(x=canvas_width + int(canvas_width / 2.5), y=2 * int(canvas_height / 4))
        b.place(x=canvas_width + int(canvas_width / 2.5), y=1 * int(canvas_height / 4))
        # b.pack()

    # def minsize(self):
    #     return 2 * canvas_width, 3 * canvas_height


def main():
    root = Tk()
    # root.geometry("500x550+450+300")
    root.geometry(str(int(large_canvas_width_coef * canvas_width)) + "x" + (
        str(int(3 * canvas_height + conv_canvas_height_coef * canvas_height))))

    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
#
# master = Tk()
#
# mainloop()
