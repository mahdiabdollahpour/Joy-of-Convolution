from constants import *


def get_normal_value(val):
    return ((val - int(canvas_height / 2)))


def denormal_value(val):
    return val + int(canvas_height / 2)
