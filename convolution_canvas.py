from constants import *

from tkinter import *

from utils import *


class ConvolutionCanvas():

    def __init__(self, signal_color, producter):
        self.signal_color = signal_color
        self.canvas_width = canvas_width * 2
        self.canvas_height = canvas_height
        self.producter = producter
        # self.producted_signal = producted_signal.copy()

        self.signal_ovals = [None for i in range(self.canvas_width)]
        self.signal = [int(canvas_height / 2) for i in range(self.canvas_width)]
        self.state = None

    def update(self):
        for ov in self.signal_ovals:
            self.w.delete(ov)
        self.signal[0] = self.producter.signal[0] - int(canvas_height / 2)
        for i in range(1, len(self.signal)):
            self.signal[i] = (self.signal[i - 1] ) + (
                    self.producter.signal[i])
        print(self.signal)
        for i in range(2 * canvas_width):
            # print(denormal_value(self.signal[i]), self.signal[i])
            self.paint(i, (self.signal[i] + int(canvas_height / 2)), i)

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
