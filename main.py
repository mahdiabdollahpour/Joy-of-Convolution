from tkinter import *
from signal_canvas import SignalCanvas

from constants import *
signal = [0 for _ in range(canvas_width)]
signals = [None for _ in range(canvas_width)]

state = None

master = Tk()
master.title("Jot of Convolution")
c1 = SignalCanvas("blue")
c1.create_canvas(master)
c2 = SignalCanvas("red")
c2.create_canvas(master)
message = Label(master, text="Draw your Signal")
message.pack(side=BOTTOM)

mainloop()
