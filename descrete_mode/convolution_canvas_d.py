from tkinter import *

from descrete_mode.constants_d import *


class ConvolutionCanvas():

    def __init__(self, canvas_width_, signal_color, producter, height_coef, scale_of_unit_of_h):
        self.hUnitScale = scale_of_unit_of_h

        self.signal_color = signal_color
        self.canvas_width = canvas_width_
        self.canvas_height = int(height_coef * canvas_height)
        self.producter = producter
        # self.producted_signal = producted_signal.copy()

        self.signal_ovals = [[] for i in range(len(self.producter.signal))]
        # self.signal = [int(canvas_height / 2) for i in range(self.canvas_width)]
        self.signal = [0 for i in range(len(self.producter.signal))]
        self.flag = [False for i in range(len(self.producter.signal))]

        self.state = None
        self.last_point = 0
        self.yellow_indexes = []

    def sum(self):
        res = 0
        print(self.producter.signal)
        # print(len(self.producter.signal))
        for signal in self.producter.signal:
            res += signal
        return res

    def update(self, at_point):
        if at_point > self.last_point:
            for i in range(self.last_point, at_point + 1):
                self.plot_conved_at_point(i, self.signal_color)
        else:
            for i in range(at_point, self.last_point + 1):
                self.plot_conved_at_point(i, self.signal_color)
        self.last_point = at_point

        self.plot_conved_at_point(at_point, highlight_color)
        for idx in self.yellow_indexes:
            self.plot_conved_at_point(idx, self.signal_color)
        self.yellow_indexes = [at_point]

    def plot_conved_at_point(self, at_point, col):
        print(at_point, self.signal)

        if self.flag[at_point] is False or col == highlight_color:
            l = len(self.producter.shifter.signal1)
            if col == self.signal_color:
                self.flag[at_point] = True
            else:
                self.flag[at_point] = False
            # self.signal[at_point] = self.sum()
            # if self.signal[at_point] is None:
            #     print("DAMNNNNNNNNNNNNNNNNNN")

            self.paint(int((self.canvas_width / 2)) + descretize_unit * (at_point),
                       (int(self.canvas_height / 2) - self.signal[at_point + l] / self.hUnitScale), at_point,
                       col)
        # if self.signal[at_point] is not None:
        #     print("value", self.signal[at_point],
        #           (int(self.canvas_height / 2) - self.signal[at_point] * convolution_diagram_unit))

    def do_conv_at(self, t):
        l = len(self.producter.shifter.signal1)
        sig1 = self.producter.shifter.signal1
        sig2 = self.producter.shifter.signal2
        val = 0
        for i in range(l):
            idx = i + t
            numer = lambda a, sig: (float(int(canvas_height / 2) - sig[a]) / unit)

            if idx >= 0 and idx < l:
                val += numer(i, sig1) * numer(idx, sig2)
        val = val * (self.producter.hUnitScale)
        return val

    def do_all_conv(self):
        l = len(self.producter.shifter.signal1)
        for t in range(-1 * l, l):
            self.signal[l + t] = self.do_conv_at(t)
            # self.signal[l + t] = 7

    def is_on_axis(self, x, y):
        if x == int(self.canvas_width / 2) or y == int(self.canvas_height / 2):
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

    def paint(self, x, y, idx, col=None):
        if col is None:
            col = self.signal_color
        index = descretize_unit * int(x / descretize_unit)
        for ov in self.signal_ovals[idx]:
            self.w.delete(ov)
        self.signal_ovals[idx] = []
        zero = int(self.canvas_height / 2)
        if y < zero:
            print("y in paint", y, zero)
            # print("zero is ", zero)
            for i in range(int(y), zero):
                x1, y1 = (index - 1), (i - 1)
                x2, y2 = (index + 1), (i + 1)
                # print("index", index)
                ov = self.w.create_oval(x1, y1, x2, y2, fill=col, outline=col)
                self.signal_ovals[idx].append(ov)
        else:
            print("y in paint", zero, int(y))
            # print("zero is ", zero)
            for i in range(zero, int(y)):
                x1, y1 = (index - 1), (i - 1)
                x2, y2 = (index + 1), (i + 1)
                # print("index", index)
                ov = self.w.create_oval(x1, y1, x2, y2, fill=col, outline=col)
                self.signal_ovals[idx].append(ov)
        # self.signal[idx] = y

    def reset(self):
        self.flag = [False for i in range(len(self.producter.signal))]
        self.last_point = 0
        for i in range(len(self.signal)):
            if self.signal_ovals[i] is not None:
                self.signal[i] = 0
                for ov in self.signal_ovals[i]:
                    self.w.delete(ov)
