from constants import *

from tkinter import *


class SignalShifter():

    def __init__(self, signal_color, signal1, signal2):
        self.signal_color = signal_color
        self.canvas_width = canvas_width * 2
        self.canvas_height = canvas_height

        self.signal1 = signal1
        self.signal1_ovals = [None for i in range(self.canvas_width)]
        self.signal2 = signal2
        self.signal2_ovals = [None for i in range(self.canvas_width)]
        self.state = None
        self.move_start = 0
        self.current_shift = 0
        self.previous_shift = 0

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
                print((event.x - self.move_start))
                self.current_shift = (event.x - self.move_start) + self.previous_shift
                self.paint(i + self.previous_shift + (event.x - self.move_start), val, i)

    def Button_lis(self, event):
        if self.state is None:
            print('a')
            self.state = "pressed"
            self.move_start = event.x
        else:
            print('b')
            self.previous_shift = self.current_shift
            self.state = None

    def out_lis(self, event):
        if self.state is not None:
            self.previous_shift = self.current_shift
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
                    print('hkj')
                    self.w.create_oval(i - 1, j - 1, i + 1, j + 1, fill="#fff")
                    # self.paint(i, j, )

    def paint(self, x, y, index, color="#476042"):
        if self.signal1_ovals[index] is not None:
            self.w.delete(self.signal1_ovals[index])

        x1, y1 = (x - 1), (y - 1)
        x2, y2 = (x + 1), (y + 1)
        self.signal1_ovals[index] = self.w.create_oval(x1, y1, x2, y2, fill=self.signal_color)
