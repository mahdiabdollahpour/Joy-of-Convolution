from tkinter import *
from descrete_mode.constants_d import *


class SignalCanvas():

    def motion_lis(self, event):
        # global state
        ## TODO : check for out of ranges
        if self.state is not None:
            # print('c')
            print("x", event.x)
            print("y", event.y)
            print((int(canvas_height / 2) - event.y) / unit)
            self.paint(event.x, event.y)
            # if event.x - 1 >= 0:
            #     self.paint(event.x - 1, event.y)
            #     if event.x - 2 >= 0:
            #         self.paint(event.x - 2, event.y)
            #         if event.x - 3 >= 0:
            #             self.paint(event.x - 3, event.y)
            #
            # if event.x + 1 < canvas_width:
            #     self.paint(event.x + 1, event.y)
            #     if event.x + 2 < canvas_width:
            #         self.paint(event.x + 2, event.y)
            #         if event.x + 3 < canvas_width:
            #             self.paint(event.x + 3, event.y)

    def Button_lis(self, event):
        if self.state is None:
            print('a')
            self.state = "pressed"
        else:
            print('b')
            self.state = None

    def out_lis(self, event):
        self.state = None

    def is_on_axis(self, x, y):
        if x == self.canvas_width / 2 or y == self.canvas_height / 2:
            return True
        return False

    def __init__(self, signal_color,scale_of_unit_of_h):
        self.hUnitScale = scale_of_unit_of_h
        self.signal_color = signal_color
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        self.signal = [int(canvas_height / 2) for i in range(int(self.canvas_width / descretize_unit))]
        self.signal_ovals = [[] for i in range(len(self.signal))]

        self.state = None

    def create_canvas(self, master):
        self.w = Canvas(master,
                        width=self.canvas_width,
                        height=self.canvas_height, highlightbackground="green",
                        highlightthickness=1, bd=0)
        self.w.pack(expand=YES, fill=BOTH)
        self.w.bind("<Button-1>", self.Button_lis)
        # self.w.bind("<Leave>", self.Button_lis)
        # w.bind("<ButtonRelease>", ButtonRelease_lis)
        self.w.bind("<Motion>", self.motion_lis)
        self.w.bind("<Leave>", self.out_lis)
        for i in range(self.canvas_width):
            for j in range(self.canvas_height):
                if (self.is_on_axis(i, j)):
                    # print('hkj')
                    self.w.create_oval(i - 1, j - 1, i + 1, j + 1, fill="#fff")
                    # self.paint(i, j, )
        self.paint_scales()


    def paint_scales(self, length1=10):
        h_zero = int(self.canvas_height / 2)
        w_zero = int(self.canvas_width / 2)
        hh = int(self.canvas_height / (2 * unit))
        for j in range(-1 * hh, hh + 1):
            for i in range(int(-1 * length1 / 2), int(length1 / 2)):
                self.w.create_oval(w_zero + i, h_zero - j * unit, w_zero + i + 1,
                                   h_zero - j * unit + 1, fill=scale_color,
                                   outline=scale_color)
                self.w.create_oval(w_zero + i, h_zero + j * unit, w_zero + i + 1,
                                   h_zero + j * unit + 1, fill=scale_color,
                                   outline=scale_color)


    def paint(self, x, y):
        index = descretize_unit * int(x / descretize_unit)
        for ov in self.signal_ovals[int(index / descretize_unit)]:
            self.w.delete(ov)
        self.signal_ovals[int(index / descretize_unit)] = []
        if y < int(canvas_height / 2):
            for i in range(int(y), int(canvas_height / 2)):
                x1, y1 = (index - 1), (i - 1)
                x2, y2 = (index + 1), (i + 1)
                # print("index", index)
                self.signal_ovals[int(index / descretize_unit)].append(
                    self.w.create_oval(x1, y1, x2, y2, fill=self.signal_color, outline=self.signal_color))
        else:
            for i in range(int(canvas_height / 2), int(y)):
                x1, y1 = (index - 1), (i - 1)
                x2, y2 = (index + 1), (i + 1)
                # print("index", index)
                self.signal_ovals[int(index / descretize_unit)].append(
                    self.w.create_oval(x1, y1, x2, y2, fill=self.signal_color, outline=self.signal_color))
        self.signal[int(index / descretize_unit)] = y

    def ramp(self, slope=2):
        self.reset()
        w = len(self.signal)
        for i in range(w):
            if i > w / 2:
                self.paint(descretize_unit * i, (-1 * slope * (((2 * i) % int(w)))) + self.canvas_height / 2)
            else:
                self.paint(descretize_unit * i, self.canvas_height / 2)

    def step(self, length=10, const=unit):
        self.reset()
        w = len(self.signal)
        for i in range(len(self.signal)):
            if i < w / 2:
                self.paint(descretize_unit * i, self.canvas_height / 2)
                # self.signal[i] = height * (i % length)
            else:
                self.paint(descretize_unit * i, self.canvas_height / 2 - const)
        print(self.signal)

    def pulse(self, length=10, height=10, const=unit):
        w = len(self.signal)
        for i in range(w):
            if i < w * 2 / 3 and i > w / 3:
                self.paint(i * descretize_unit, self.canvas_height / 2 - const)
                # self.signal[i] = height * (i % length)
            else:
                self.paint(i * descretize_unit, self.canvas_height / 2)
                # self.signal[i] = height * (((length - i) % length))

    def reset(self):
        for i in range(len(self.signal)):
            self.signal[i] = self.canvas_height / 2
            if self.signal_ovals[i] is not None:
                for ov in self.signal_ovals[i]:
                    self.w.delete(ov)
