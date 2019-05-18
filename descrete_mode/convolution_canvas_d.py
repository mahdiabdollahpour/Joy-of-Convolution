from tkinter import *

from descrete_mode.constants_d import *


class ConvolutionCanvas():

    def __init__(self, canvas_width_, signal_color, producter, height_coef):
        self.signal_color = signal_color
        self.canvas_width = canvas_width_
        self.canvas_height = int(height_coef * canvas_height)
        self.producter = producter
        # self.producted_signal = producted_signal.copy()

        self.signal_ovals = [[] for i in range(len(self.producter.signal))]
        # self.signal = [int(canvas_height / 2) for i in range(self.canvas_width)]
        self.signal = [None for i in range(len(self.producter.signal))]
        self.state = None

    def sum(self):
        res = 0
        print(self.producter.signal)
        # print(len(self.producter.signal))
        for signal in self.producter.signal:
            res += signal
        return res

    def update(self, at_point):
        # print("in update", at_point, self.signal[at_point])
        self.plot_conved_at_point(at_point)

    def plot_conved_at_point(self, at_point):
        # print(at_point,len(self.signal))

        if self.signal[at_point] is None:
            self.signal[at_point] = self.sum()
            # if self.signal[at_point] is None:
            #     print("DAMNNNNNNNNNNNNNNNNNN")

            self.paint(int((self.canvas_width / 2)) + descretize_unit * at_point,
                       (int(self.canvas_height / 2) - self.signal[at_point] * convolution_diagram_unit), at_point)
        if  self.signal[at_point] is not None:
            print("value", self.signal[at_point],
                  (int(self.canvas_height / 2) - self.signal[at_point] * convolution_diagram_unit))

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

    def paint(self, x, y, idx):
        index = descretize_unit * int(x / descretize_unit)
        for ov in self.signal_ovals[idx]:
            self.w.delete(ov)
        self.signal_ovals[idx] = []
        if y < int(canvas_height / 2):
            for i in range(int(y), int(self.canvas_height / 2)):
                x1, y1 = (index - 1), (i - 1)
                x2, y2 = (index + 1), (i + 1)
                # print("index", index)
                self.signal_ovals[idx].append(
                    self.w.create_oval(x1, y1, x2, y2, fill=self.signal_color, outline=self.signal_color))
        else:
            for i in range(int(self.canvas_height / 2), int(y)):
                x1, y1 = (index - 1), (i - 1)
                x2, y2 = (index + 1), (i + 1)
                # print("index", index)
                self.signal_ovals[idx].append(
                    self.w.create_oval(x1, y1, x2, y2, fill=self.signal_color, outline=self.signal_color))
        # self.signal[idx] = y




    def reset(self):
        for i in range(len(self.signal)):
            if self.signal_ovals[i] is not None:
                self.signal[i] = None
                for ov in self.signal_ovals[i]:
                    self.w.delete(ov)