from descrete_mode.constants_d import *

from tkinter import *


class ProductCanvas():
    def __init__(self, canvas_width_, signal_color, shifter, scale_of_unit_of_h):
        self.hUnitScale = scale_of_unit_of_h
        self.shifter = shifter
        self.signal_color = signal_color
        self.canvas_width = canvas_width_
        self.canvas_height = canvas_height

        self.signal = [0 for i in range(int(self.canvas_width / descretize_unit))]
        self.signal_ovals = [[] for i in range(int(self.canvas_width / descretize_unit))]

        self.state = None

    def round(self, val):
        if (val % descretize_unit) < descretize_unit / 2:
            return descretize_unit * int(val / descretize_unit)
        else:
            return descretize_unit * int((val / descretize_unit) + 1)

    def update(self, shift):
        for ov in self.signal_ovals:
            self.w.delete(ov)
        for i in range(len(self.shifter.signal2)):
            index = - 1 * shift + i
            # print("at index", i)
            shifted_value = 0
            if index < len(self.shifter.signal1) and index >= 0:
                shifted_value = ((int(canvas_height / 2) - self.shifter.signal1[index]) / unit)
            stable_value = ((int(canvas_height / 2) - self.shifter.signal2[i]) / unit)
            # stable_value = 1
            self.signal[i] = shifted_value * stable_value \
                             * (self.shifter.canvas1.hUnitScale * self.shifter.canvas2.hUnitScale) / self.hUnitScale
            # print(self.shifter.signal1)

            # print("its in update", self.signal[i])
            self.paint(descretize_unit * i + int((self.canvas_width / 2) - (canvas_width / 2)),
                       int(canvas_height / 2) - self.signal[i] * unit, i)
        # for j in range(len(self.signal)):

    def is_on_axis(self, x, y):
        if x == self.canvas_width / 2 or y == self.canvas_height / 2:
            return True
        return False

    def create_canvas(self, master):
        self.w = Canvas(master,
                        width=self.canvas_width,
                        height=self.canvas_height, highlightbackground="green",
                        highlightthickness=1, bd=0)
        self.w.pack(expand=YES, fill=BOTH)

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

    def paint(self, x, y, index):
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
        # self.signal[int(index / descretize_unit)] = y

    def reset(self):
        for i in range(len(self.signal)):
            if self.signal_ovals[i] is not None:
                self.signal[i] = 0
                for ov in self.signal_ovals[i]:
                    self.w.delete(ov)
