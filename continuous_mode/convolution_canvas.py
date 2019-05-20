from tkinter import *

from continuous_mode.utils import *


class ConvolutionCanvas():

    def __init__(self, canvas_width_, signal_color, producter, height_coef):
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

    def sum(self):
        res = 0
        print(self.producter.signal)
        for signal in self.producter.signal:
            res += signal
        return res

    def update(self, at_point):
        if at_point > self.last_point:
            for i in range(self.last_point, at_point):
                self.plot_conved_at_point(i)
        else:
            for i in range(at_point, self.last_point):
                self.plot_conved_at_point(i)
        self.last_point = at_point

    def plot_conved_at_point(self, at_point):
        print(at_point, self.signal)
        if self.flag[at_point] is False:
            l = len(self.producter.shifter.signal1)

            self.flag[at_point] = True
            # self.signal[at_point] = self.sum()
            # if self.signal[at_point] is None:
            #     print("DAMNNNNNNNNNNNNNNNNNN")
            # print(self.signal[at_point],
            #       (int(self.canvas_height / 2) - self.signal[at_point] * convolution_diagram_unit))
            self.paint(int((self.canvas_width / 2)) + at_point,
                       (int(self.canvas_height / 2) - self.signal[at_point + l] * convolution_diagram_unit), at_point)

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

    def paint(self, x, y, index):
        if self.signal_ovals[index] is not None:
            self.w.delete(self.signal_ovals[index])

        x1, y1 = (x - 1), (y - 1)
        x2, y2 = (x + 1), (y + 1)
        self.signal_ovals[index] = self.w.create_oval(x1, y1, x2, y2, fill=self.signal_color, outline=self.signal_color)

    def reset(self):
        for index in range(self.canvas_width):
            if self.signal_ovals[index] is not None:
                self.w.delete(self.signal_ovals[index])
            self.signal[index] = None
