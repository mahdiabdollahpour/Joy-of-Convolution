from constants import *

from tkinter import *


class ProductCanvas():
    def __init__(self, canvas_width_, signal_color, shifter):
        self.shifter = shifter
        self.signal_color = signal_color
        self.canvas_width = canvas_width_
        self.canvas_height = canvas_height

        self.signal = [0 for i in range(self.canvas_width)]
        self.signal_ovals = [None for i in range(self.canvas_width)]

        self.state = None

    def update(self):
        for ov in self.signal_ovals:
            self.w.delete(ov)
        for i in range(canvas_width):
            index = - 1 * self.shifter.total_shift + i
            # print("at index", i)
            shifted_value = 0
            if index < len(self.shifter.signal1) and index >= 0:
                shifted_value = ((int(canvas_height / 2) - self.shifter.signal1[index]) / unit)
            stable_value = ((int(canvas_height / 2) - self.shifter.signal2[i]) / unit)
            # stable_value = 1
            self.signal[i] = shifted_value * stable_value
            # print(self.shifter.signal1)

            # print("its in update", self.signal[i])
            self.paint(i + int((self.canvas_width / 2) - (canvas_width / 2)),
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

    def paint(self, x, y, index):
        if self.signal_ovals[index] is not None:
            self.w.delete(self.signal_ovals[index])

        x1, y1 = (x - 1), (y - 1)
        x2, y2 = (x + 1), (y + 1)
        self.signal_ovals[index] = self.w.create_oval(x1, y1, x2, y2, fill=self.signal_color)
