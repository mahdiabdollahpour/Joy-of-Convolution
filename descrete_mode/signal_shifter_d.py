from descrete_mode.constants_d import *

from tkinter import *


class SignalShifter():

    def __init__(self, canvas_width_, signal_color, signal1, signal2, product_canvas, conv_canvas):
        self.signal_color = signal_color
        self.canvas_width = canvas_width_
        self.canvas_height = canvas_height
        self.pc = product_canvas
        self.cc = conv_canvas

        self.signal1 = signal1.copy()
        self.signal1_ovals = [[] for i in range(len(self.signal1))]
        self.signal2 = signal2.copy()
        self.signal2_ovals = [[] for i in range(len(self.signal2))]
        self.state = None
        self.move_start = int(self.canvas_width / 2)
        self.current_shift = 0
        self.previous_shift = 0

    def round(self, val):
        if (val % descretize_unit) < descretize_unit / 2:
            return descretize_unit * int(val / descretize_unit)
        else:
            return descretize_unit * int((val / descretize_unit) + 1)

    def is_on_axis(self, x, y):
        if x == self.canvas_width / 2 or y == self.canvas_height / 2:
            return True
        return False

    def motion_lis(self, event):
        # global state
        ## TODO : check for out of ranges
        if self.state is not None:
            # for oval in self.signal1_ovals:
            #     self.w.delete(oval)
            for i, val in enumerate(self.signal1):
                # self.w.delete(self.signal1_ovals[i])
                # print((event.x - self.move_start))
                self.current_shift = (event.x - self.move_start)
                self.total_shift = self.current_shift + self.previous_shift
                # print("Current shift", self.current_shift)
                # print("previous_shift", self.previous_shift)
                # print("total_shift", self.total_shift)

                self.paint(descretize_unit * i + int((self.canvas_width / 2) - (canvas_width / 2)) + self.total_shift,
                           val,
                           i,
                           signal_idx=1)
            self.pc.update()

            self.cc.update(int(self.total_shift / descretize_unit))

    # def do_all_convs(self):
    # l = len(self.signal2)
    # for i in range(-1 * l, l):
    #     self.cc.update(l)

    def Button_lis(self, event):
        if self.state is None:
            print('a')
            self.state = "pressed"
            self.move_start = event.x
        else:
            print('b')
            self.previous_shift = self.total_shift
            # self.move_start = event.x
            self.state = None

    def out_lis(self, event):
        if self.state is not None:
            self.previous_shift = self.total_shift
        self.state = None

    def create_canvas(self, master):
        self.w = Canvas(master,
                        width=self.canvas_width,
                        height=self.canvas_height, highlightbackground="green",
                        highlightthickness=1, bd=0)
        self.w.pack(expand=YES, fill=BOTH)
        self.w.bind("<Button-1>", self.Button_lis)

        self.w.bind("<Motion>", self.motion_lis)
        self.w.bind("<Leave>", self.out_lis)
        for i in range(self.canvas_width):
            for j in range(self.canvas_height):
                if (self.is_on_axis(i, j)):
                    # print('hkj')
                    self.w.create_oval(i - 1, j - 1, i + 1, j + 1, fill="#fff")
                    # self.paint(i, j, )

    def plot(self):
        self.current_shift = 0
        self.previous_shift = 0
        for i, sing in enumerate(self.signal1):
            print("Hey there")
            self.paint(i * descretize_unit + int((self.canvas_width / 2) - (canvas_width / 2)), sing, i, signal_idx=1,
                       color="blue")
        for i, sing in enumerate(self.signal2):
            self.paint(i * descretize_unit + int((self.canvas_width / 2) - (canvas_width / 2)), sing, i, signal_idx=2,
                       color="red")

    def paint(self, x, y, idx, signal_idx, color="#476042"):
        if signal_idx == 1:
            index = descretize_unit * int(x / descretize_unit)
            for ov in self.signal1_ovals[idx]:
                self.w.delete(ov)
            self.signal1_ovals[idx] = []
            if y < int(canvas_height / 2):
                for i in range(int(y), int(canvas_height / 2)):
                    x1, y1 = (index - 1), (i - 1)
                    x2, y2 = (index + 1), (i + 1)
                    # print("index", index)
                    self.signal1_ovals[idx].append(
                        self.w.create_oval(x1, y1, x2, y2, fill="red", outline="red"))
            else:
                for i in range(int(canvas_height / 2), int(y)):
                    x1, y1 = (index - 1), (i - 1)
                    x2, y2 = (index + 1), (i + 1)
                    # print("index", index)
                    self.signal1_ovals[idx].append(
                        self.w.create_oval(x1, y1, x2, y2, fill="red", outline="red"))
            # self.signal1[idx] = y

        else:
            index = descretize_unit * int(x / descretize_unit)
            for ov in self.signal2_ovals[idx]:
                self.w.delete(ov)
            self.signal2_ovals[idx] = []
            if y < int(canvas_height / 2):
                for i in range(int(y), int(canvas_height / 2)):
                    x1, y1 = (index - 1), (i - 1)
                    x2, y2 = (index + 1), (i + 1)
                    # print("index", index)
                    self.signal2_ovals[idx].append(
                        self.w.create_oval(x1, y1, x2, y2, fill="blue", outline="blue"))
            else:
                for i in range(int(canvas_height / 2), int(y)):
                    x1, y1 = (index - 1), (i - 1)
                    x2, y2 = (index + 1), (i + 1)
                    # print("index", index)
                    self.signal2_ovals[idx].append(
                        self.w.create_oval(x1, y1, x2, y2, fill="blue", outline="blue"))
            # self.signal2[idx] = y

    def reset(self):
        for i in range(len(self.signal1)):
            if self.signal1_ovals[i] is not None:
                for ov in self.signal1_ovals[i]:
                    self.w.delete(ov)

        for i in range(len(self.signal2)):
            if self.signal2_ovals[i] is not None:
                for ov in self.signal2_ovals[i]:
                    self.w.delete(ov)
