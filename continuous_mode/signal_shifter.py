from continuous_mode.constants import *

from tkinter import *


class SignalShifter():

    def __init__(self, canvas_width_, signal_color1, signal_color2, signal1, signal2, product_canvas, conv_canvas):
        self.signal_color1 = signal_color1
        self.signal_color2 = signal_color2
        self.canvas_width = canvas_width_
        self.canvas_height = canvas_height
        self.pc = product_canvas
        self.cc = conv_canvas

        self.signal1 = signal1.copy()
        self.signal1_ovals = [None for i in range(self.canvas_width)]
        self.signal2 = signal2.copy()
        self.signal2_ovals = [None for i in range(self.canvas_width)]
        self.state = None
        self.move_start = int(self.canvas_width / 2)
        self.current_shift = 0
        self.previous_shift = 0

    def is_on_axis(self, x, y):
        if x == self.canvas_width / 2 or y == self.canvas_height / 2:
            return True
        return False

    def motion_lis(self, event):
        # global state
        ## TODO : check for out of ranges
        if self.state is not None:
            # for oval in self.signal1_ovals:
            #     self.w.delete(oval)
            for i, val in enumerate(self.signal1):
                # self.w.delete(self.signal1_ovals[i])
                # print((event.x - self.move_start))
                self.current_shift = (event.x - self.move_start)
                self.total_shift = self.current_shift + self.previous_shift
                # print("Current shift", self.current_shift)
                # print("previous_shift", self.previous_shift)
                # print("total_shift", self.total_shift)
                self.paint(i + int((self.canvas_width / 2) - (canvas_width / 2)) + self.total_shift, val,
                           i,
                           signal_idx=1)
            self.pc.update()
            self.cc.update(self.total_shift)

    def Button_lis(self, event):
        if self.state is None:
            print('a')
            self.state = "pressed"
            self.move_start = event.x
        else:
            print('b')
            self.previous_shift = self.total_shift
            # self.move_start = event.x
            self.state = None

    def out_lis(self, event):
        if self.state is not None:
            self.previous_shift = self.total_shift
        self.state = None

    def create_canvas(self, master):
        self.w = Canvas(master,
                        width=self.canvas_width,
                        height=self.canvas_height, highlightbackground="green",
                        highlightthickness=1, bd=0)
        self.w.pack(expand=YES, fill=BOTH)
        self.w.bind("<Button-1>", self.Button_lis)

        self.w.bind("<Motion>", self.motion_lis)
        self.w.bind("<Leave>", self.out_lis)
        for i in range(self.canvas_width):
            for j in range(self.canvas_height):
                if (self.is_on_axis(i, j)):
                    # print('hkj')
                    self.w.create_oval(i - 1, j - 1, i + 1, j + 1, fill="#fff")
        self.paint_scales()  # self.paint(i, j, )

    def paint_scales(self, length1=10, length2=10, width_unit=40):
        h_zero = int(self.canvas_height / 2)
        w_zero = int(self.canvas_width / 2)
        for i in range(int(-1 * length1 / 2), int(length1 / 2)):
            self.w.create_oval(w_zero + i - 1, h_zero - unit - 1, w_zero + i + 1, h_zero - unit + 1, fill=scale_color,
                               outline=scale_color)
            self.w.create_oval(w_zero + i - 1, h_zero + unit - 1, w_zero + i + 1, h_zero + unit + 1, fill=scale_color,
                               outline=scale_color)

        ww = int(self.canvas_width / (2 * width_unit))
        for i in range(-1 * ww, ww + 1):
            for j in range(int(-1 * length2 / 2), int(length2 / 2)):
                self.w.create_oval(w_zero + width_unit * i - 1, h_zero + j - 1, w_zero + width_unit * i + 1,
                                   h_zero + j + 1, fill=scale_color,
                                   outline=scale_color)

    def plot(self):
        self.current_shift = 0
        self.previous_shift = 0
        for i, sing in enumerate(self.signal1):
            print("Hey there")
            self.paint(i + int((self.canvas_width / 2) - (canvas_width / 2)), sing, i, signal_idx=1)
        for i, sing in enumerate(self.signal2):
            self.paint(i + int((self.canvas_width / 2) - (canvas_width / 2)), sing, i, signal_idx=2)

    def paint(self, x, y, index, signal_idx):
        if signal_idx == 1:

            if self.signal1_ovals[index] is not None:
                self.w.delete(self.signal1_ovals[index])

            x1, y1 = (x - 1), (y - 1)
            x2, y2 = (x + 1), (y + 1)
            self.signal1_ovals[index] = self.w.create_oval(x1, y1, x2, y2, fill=self.signal_color1,
                                                           outline=self.signal_color1)

        else:
            if self.signal2_ovals[index] is not None:
                self.w.delete(self.signal2_ovals[index])
            x1, y1 = (x - 1), (y - 1)
            x2, y2 = (x + 1), (y + 1)
            self.signal2_ovals[index] = self.w.create_oval(x1, y1, x2, y2, fill=self.signal_color2,
                                                           outline=self.signal_color2)

    def reset(self):
        for index in range(self.canvas_width):
            # self.signal1[index] = self.canvas_height / 2
            if self.signal1_ovals[index] is not None:
                self.w.delete(self.signal1_ovals[index])

        for index in range(self.canvas_width):
            # self.signal2[index] = self.canvas_height / 2
            if self.signal2_ovals[index] is not None:
                self.w.delete(self.signal2_ovals[index])
