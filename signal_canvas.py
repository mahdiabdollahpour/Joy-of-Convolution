from tkinter import *
from constants import *

class SignalCanvas():

    def motion_lis(self, event):
        # global state
        ## TODO : check for out of ranges
        if self.state is not None:
            # print('c')
            self.paint(event.x, event.y)
            self.paint(event.x - 1, event.y)
            self.paint(event.x - 2, event.y)
            self.paint(event.x - 3, event.y)
            self.paint(event.x + 1, event.y)
            self.paint(event.x + 2, event.y)
            self.paint(event.x + 3, event.y)

    def Button_lis(self, event):
        if self.state is None:
            print('a')
            self.state = "pressed"
        else:
            print('b')
            self.state = None

    def out_lis(self, event):
        self.state = None

    def is_on_axis(self, x, y):
        if x == self.canvas_width / 2 or y == self.canvas_height / 2:
            return True
        return False

    def __init__(self, signal_color):
        self.signal_color = signal_color
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        self.signal = [0 for i in range(self.canvas_width)]
        self.signals = [None for i in range(self.canvas_width)]

        self.state = None

    def create_canvas(self, master):
        self.w = Canvas(master,
                        width=self.canvas_width,
                        height=self.canvas_height, highlightbackground="green",
                        highlightthickness=1, bd=0)
        self.w.pack(expand=YES, fill=BOTH)
        self.w.bind("<Button-1>", self.Button_lis)
        # self.w.bind("<Leave>", self.Button_lis)
        # w.bind("<ButtonRelease>", ButtonRelease_lis)
        self.w.bind("<Motion>", self.motion_lis)
        self.w.bind("<Leave>", self.out_lis)
        for i in range(self.canvas_width):
            for j in range(self.canvas_height):
                if (self.is_on_axis(i, j)):
                    print('hkj')
                    self.w.create_oval(i - 1, j - 1, i + 1, j + 1, fill="#fff")
                    # self.paint(i, j, )

    def paint(self, x, y, color="#476042"):
        if self.signals[x - 1] is not None:
            self.w.delete(self.signals[x - 1])

        x1, y1 = (x - 1), (y - 1)
        x2, y2 = (x + 1), (y + 1)
        self.signal[x - 1] = y
        self.signals[x - 1] = self.w.create_oval(x1, y1, x2, y2, fill=self.signal_color)
