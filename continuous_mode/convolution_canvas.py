from tkinter import *

from continuous_mode.utils import *


class ConvolutionCanvas():

    def __init__(self, canvas_width_, signal_color, producter, height_coef, scale_of_unit_of_h):
        self.hUnitScale = scale_of_unit_of_h
        self.signal_color = signal_color
        self.canvas_width = canvas_width_
        self.canvas_height = int(height_coef * canvas_height)
        self.producter = producter
        # self.producted_signal = producted_signal.copy()

        self.signal_ovals = [None for i in range(self.canvas_width)]
        # self.signal = [int(canvas_height / 2) for i in range(self.canvas_width)]
        self.flag = [False for i in range(self.canvas_width)]

        self.signal = [0 for i in range(self.canvas_width)]
        self.state = None
        self.last_point = 0
        self.yellow_indexes = []

    def sum(self):
        res = 0
        print(self.producter.signal)
        for signal in self.producter.signal:
            res += signal
        return res

    def update(self, at_point):
        # if at_point > self.last_point:
        #     for i in range(self.last_point, at_point):
        #         self.plot_conved_at_point(i)
        # else:
        #     for i in range(at_point, self.last_point):
        #         self.plot_conved_at_point(i)
        # self.last_point = at_point

        if at_point > self.last_point:
            for i in range(self.last_point, at_point):
                self.plot_conved_at_point(i, self.signal_color)
        else:
            for i in range(at_point, self.last_point):
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
            # print(self.signal[at_point],
            #       (int(self.canvas_height / 2) - self.signal[at_point] * convolution_diagram_unit))
            self.paint(int((self.canvas_width / 2)) + at_point,
                       (int(self.canvas_height / 2) - self.signal[at_point + l] / self.hUnitScale), at_point, col)

    def do_conv_at(self, t):
        l = len(self.producter.shifter.signal1)
        sig1 = self.producter.shifter.signal1
        sig2 = self.producter.shifter.signal2
        val = 0
        for i in range(l):
            idx = i + t
            numer = lambda a, sig: ((int(canvas_height / 2) - sig[a]) / unit)
            if idx >= 0 and idx < l:
                val += numer(i, sig1) * numer(idx, sig2)
        val = val * (self.producter.hUnitScale)
        return val

    def do_all_conv(self):
        sig1 = self.producter.shifter.signal1
        sig2 = self.producter.shifter.signal2
        print(sig1)
        print(sig2)
        l = len(self.producter.shifter.signal1)
        for t in range(-1 * l, l):
            self.signal[l + t] = self.do_conv_at(t)

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

    # def paint_scales(self, length1=10, length2=10, width_unit=30):
    #     h_zero = int(self.canvas_height / 2)
    #     w_zero = int(self.canvas_width / 2)
    #     for i in range(int(-1 * length1 / 2), int(length1 / 2)):
    #         self.w.create_oval(w_zero + i - 1, h_zero - unit - 1, w_zero + i + 1, h_zero - unit + 1, fill=scale_color,
    #                            outline=scale_color)
    #         self.w.create_oval(w_zero + i - 1, h_zero + unit - 1, w_zero + i + 1, h_zero + unit + 1, fill=scale_color,
    #                            outline=scale_color)
    #
    #     ww = int(self.canvas_width / (2 * width_unit))
    #     for i in range(-1 * ww, ww + 1):
    #         for j in range(int(-1 * length2 / 2), int(length2 / 2)):
    #             self.w.create_oval(w_zero + width_unit * i - 1, h_zero + j - 1, w_zero + width_unit * i + 1,
    #                                h_zero + j + 1, fill=scale_color,
    #                                outline=scale_color)

    def paint(self, x, y, index, col=None):
        if col is None:
            col = self.signal_color
        if col == highlight_color:
            r = 5
        else:
            r = 1
        if self.signal_ovals[index] is not None:
            self.w.delete(self.signal_ovals[index])

        x1, y1 = (x - r), (y - r)
        x2, y2 = (x + r), (y + r)
        self.signal_ovals[index] = self.w.create_oval(x1, y1, x2, y2, fill=col, outline=col)

    def reset(self):
        self.flag = [False for i in range(self.canvas_width)]
        self.last_point = 0
        for index in range(self.canvas_width):

            if self.signal_ovals[index] is not None:
                self.w.delete(self.signal_ovals[index])
            self.signal[index] = 0
