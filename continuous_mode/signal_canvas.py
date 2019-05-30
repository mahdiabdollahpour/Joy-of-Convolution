from tkinter import *
from continuous_mode.constants import *

pressed = "pressed"
line = "line"


class SignalCanvas():

    def motion_lis(self, event):
        # global state
        ## TODO : check for out of ranges
        if self.state == pressed:
            # print('c')
            print("x", event.x)
            print("y", event.y)
            print((int(canvas_height / 2) - event.y) / unit)
            self.paint(event.x, event.y)
            if event.x - 1 >= 0:
                self.paint(event.x - 1, event.y)
                if event.x - 2 >= 0:
                    self.paint(event.x - 2, event.y)
                    if event.x - 3 >= 0:
                        self.paint(event.x - 3, event.y)

            if event.x + 1 < canvas_width:
                self.paint(event.x + 1, event.y)
                if event.x + 2 < canvas_width:
                    self.paint(event.x + 2, event.y)
                    if event.x + 3 < canvas_width:
                        self.paint(event.x + 3, event.y)

    def Button_lis(self, event):
        if self.state is None:
            print('a')
            if self.mode == 1:
                self.state = pressed
            else:
                self.state = line
                self.start_line_x = event.x
                self.start_line_y = event.y
        else:
            print('b')
            if self.state == line:
                self.draw_line(event)
            self.state = None

    def draw_line(self, event):
        x1 = self.start_line_x
        y1 = self.start_line_y
        x2 = event.x
        y2 = event.y
        if x1 < x2:
            slope = (y2 - y1) / (x2 - x1)
            for i in range(x1, x2):
                self.paint(i, (i - x1) * slope + y1)
        else:
            slope = (y1 - y2) / (x1 - x2)
            for i in range(x2, x1):
                self.paint(i, (i - x2) * slope + y2)

    def out_lis(self, event):
        self.state = None

    def is_on_axis(self, x, y):
        if x == self.canvas_width / 2 or y == self.canvas_height / 2:
            return True
        return False

    def __init__(self, signal_color, scale_of_unit_of_h, mode):
        self.mode = mode
        self.hUnitScale = scale_of_unit_of_h
        self.signal_color = signal_color
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        self.signal = [int(canvas_height / 2) for i in range(self.canvas_width)]
        self.signal_ovals = [None for i in range(self.canvas_width)]

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
        self.paint_scales()  # self.paint(i, j, )

    def paint_scales(self, length1=10, length2=10, width_unit=40):
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

        ww = int(self.canvas_width / (2 * width_unit))
        for i in range(-1 * ww, ww + 1):
            for j in range(int(-1 * length2 / 2), int(length2 / 2)):
                self.w.create_oval(w_zero + width_unit * i - 1, h_zero + j - 1, w_zero + width_unit * i + 1,
                                   h_zero + j + 1, fill=scale_color,
                                   outline=scale_color)

    def paint(self, x, y, color="#476042"):
        if self.signal_ovals[x - 1] is not None:
            self.w.delete(self.signal_ovals[x - 1])

        x1, y1 = (x - 1), (y - 1)
        x2, y2 = (x + 1), (y + 1)
        self.signal[x - 1] = y
        self.signal_ovals[x - 1] = self.w.create_oval(x1, y1, x2, y2, fill=self.signal_color, outline=self.signal_color)

    def ramp(self, slope=0.5):
        self.reset()
        for i in range(self.canvas_width):
            if i > canvas_width / 2:
                self.paint(i, (-1 * slope * ((i % int(canvas_width / 2)))) + self.canvas_height / 2)
            else:
                self.paint(i, self.canvas_height / 2)

    def step(self, length=40, const=unit):
        self.reset()

        for i in range(self.canvas_width):
            if i < canvas_width / 2:
                self.paint(i, self.canvas_height / 2)
            else:
                self.paint(i, self.canvas_height / 2 - const)

    def pulse(self):

        self.reset()
        const = unit
        w = self.canvas_width
        h = self.canvas_height
        for i in range(w):
            if i > (w / 3) and i < (w / 2):
                self.paint(i, h / 2 - const)
                # print("dkjfdkfjlkdf")
            elif i > (w / 2) and i < (w * (2 / 3)):
                self.paint(i, h / 2 - const)
            else:
                self.paint(i, h / 2)

    def reset(self):
        ## TODO: clear value
        for index in range(self.canvas_width):
            self.signal[index] = self.canvas_height / 2
            if self.signal_ovals[index] is not None:
                self.w.delete(self.signal_ovals[index])
