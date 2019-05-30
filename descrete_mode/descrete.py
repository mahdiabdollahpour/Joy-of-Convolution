from descrete_mode.signal_canvas_d import SignalCanvas
from descrete_mode.signal_shifter_d import SignalShifter
from descrete_mode.product_canvas_d import ProductCanvas
from descrete_mode.convolution_canvas_d import *
# signal = [0 for _ in range(canvas_width)]
# signals = [None for _ in range(canvas_width)]

# state = None


# from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label

## TODO : add some predefined signals , clear button to clear all, shifter moves suddenly after first click
conv_canvas_height_coef = 1.5


class Example(Frame):

    def __init__(self):
        super().__init__(width=2 * canvas_width+ options_width, height=canvas_height * 4)

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
        self.master.title("Jot of Convolution")
        self.c1 = SignalCanvas("blue", scale_of_unit_of_h=h_unit_scale_signal1)
        self.c1.create_canvas(self.master)
        self.c2 = SignalCanvas("red", scale_of_unit_of_h=h_unit_scale_signal2)
        self.c2.create_canvas(self.master)
        self.pc = ProductCanvas(int(large_canvas_width_coef * canvas_width), "red", None,
                                scale_of_unit_of_h=h_unit_scale_producter)
        self.cc = ConvolutionCanvas(int(large_canvas_width_coef * canvas_width), "blue", self.pc,
                                    conv_canvas_height_coef, scale_of_unit_of_h=h_unit_scale_convolution)
        self.ssh = SignalShifter(int(large_canvas_width_coef * canvas_width), self.c1,
                                 self.c2,
                                 self.pc, self.cc, scale_of_unit_of_h=h_unit_scale_shifter)
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

        message = Label(self.master)
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



        entry_width = 50

        l1 = tk.Label(self.master, text="Scale 1:")
        self.signal1_scale_inp = tk.Entry(self.master)
        # signal1_scale_inp.
        l1.place(x=large_canvas_width_coef * canvas_width + 5, y=0)
        self.signal1_scale_inp.place(x=large_canvas_width_coef * canvas_width + 5, y=30, width=entry_width)
        self.signal1_scale_inp.insert(0, str(h_unit_scale_signal1))

        l2 = tk.Label(self.master, text="Scale 2:")
        self.signal2_scale_inp = tk.Entry(self.master)
        l2.place(x=large_canvas_width_coef * canvas_width + 5, y=canvas_height / 2)
        self.signal2_scale_inp.place(x=large_canvas_width_coef * canvas_width + 5, y=30 + canvas_height / 2,
                                     width=entry_width)
        self.signal2_scale_inp.insert(0, str(h_unit_scale_signal2))

        l4 = tk.Label(self.master, text="Scale:")
        self.shifter_scale_inp = tk.Entry(self.master)
        l4.place(x=large_canvas_width_coef * canvas_width + 5, y=canvas_height)
        self.shifter_scale_inp.place(x=large_canvas_width_coef * canvas_width + 5, y=30 + canvas_height,
                                     width=entry_width)
        self.shifter_scale_inp.insert(0, str(h_unit_scale_shifter))

        l3 = tk.Label(self.master, text="Scale:")
        self.producter_scale_inp = tk.Entry(self.master)
        l3.place(x=large_canvas_width_coef * canvas_width + 5, y=2 * canvas_height)
        self.producter_scale_inp.place(x=large_canvas_width_coef * canvas_width + 5, y=30 + 2 * canvas_height,
                                       width=entry_width)
        self.producter_scale_inp.insert(0, str(h_unit_scale_producter))

        l5 = tk.Label(self.master, text="Scale:")
        self.conv_scale_inp = tk.Entry(self.master)
        l5.place(x=large_canvas_width_coef * canvas_width + 5, y=3 * canvas_height)
        self.conv_scale_inp.place(x=large_canvas_width_coef * canvas_width + 5, y=30 + 3 * canvas_height,
                                  width=entry_width)
        self.conv_scale_inp.insert(0, str(h_unit_scale_convolution))

        apply_scales = Button(self.master, text="Apply Scales", command=self.apply_scales, height=1, width=10)
        apply_scales.place(x=large_canvas_width_coef * canvas_width + 10, y=4 * canvas_height - 30)

    def apply_scales(self):
        self.c1.hUnitScale = float(self.signal1_scale_inp.get())
        self.c2.hUnitScale = float(self.signal2_scale_inp.get())
        self.cc.hUnitScale = float(self.conv_scale_inp.get())
        self.ssh.hUnitScale = float(self.shifter_scale_inp.get())
        self.pc.hUnitScale = float(self.producter_scale_inp.get())
        # b.pack()

    # def minsize(self):
    #     return 2 * canvas_width, 3 * canvas_height


def main():
    root = Tk()
    # root.geometry("500x550+450+300")
    root.geometry(str(int(large_canvas_width_coef * canvas_width+ options_width)) + "x" + (
        str(int(3 * canvas_height + conv_canvas_height_coef * canvas_height))))

    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
#
# master = Tk()
#
# mainloop()
