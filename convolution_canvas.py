from constants import *

from tkinter import *

from utils import *
import numpy as np


class ConvolutionCanvas():

    def __init__(self,canvas_width_, signal_color, producter):
        self.signal_color = signal_color
        self.canvas_width = canvas_width_
        self.canvas_height = canvas_height
        self.producter = producter
        # self.producted_signal = producted_signal.copy()

        self.signal_ovals = [None for i in range(self.canvas_width)]
        # self.signal = [int(canvas_height / 2) for i in range(self.canvas_width)]
        self.signal = [None for i in range(self.canvas_width)]
        self.state = None

    def sum(self):
        res = 0
        print(self.producter.signal)
        for signal in self.producter.signal:
            res += signal
        return res

    def update(self, at_point):
        self.plot_conved_at_point(at_point)

    def plot_conved_at_point(self, at_point):
        if self.signal[at_point] is None:
            self.signal[at_point] = self.sum()
            if self.signal[at_point] is None:
                print("DAMNNNNNNNNNNNNNNNNNN")
            print(self.signal[at_point])
            self.paint(int((self.canvas_width / 2) - (canvas_width / 2)) + at_point, (int(canvas_height / 2) - self.signal[at_point] * convolution_diagram_unit), at_point)

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

    def paint(self, x, y, index):
        if self.signal_ovals[index] is not None:
            self.w.delete(self.signal_ovals[index])

        x1, y1 = (x - 1), (y - 1)
        x2, y2 = (x + 1), (y + 1)
        self.signal_ovals[index] = self.w.create_oval(x1, y1, x2, y2, fill=self.signal_color)
