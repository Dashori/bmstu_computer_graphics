from tkinter import *
from tkinter import messagebox
import ui
import methods
from colormap import rgb2hex
from math import pi, cos, sin, radians

const_x = 400
const_y = 350

def add_point_field_int(field_x, field_y):
    try:
        x=int(field_x.get())
        y=int(field_y.get())
        return x, y
    except:
        messagebox.showerror('Ошибка','Координаты точки- целые числа')
        return -1
    
    
def create_segment(option, color):
    rc_1 = add_point_field_int(ui.add_point_entry_xn, ui.add_point_entry_yn)
    
    if (rc_1 != -1):
        xn, yn = rc_1[0], rc_1[1]
    else:
        return

    rc_2 = add_point_field_int(ui.add_point_entry_xk, ui.add_point_entry_yk)
    
    if (rc_2 != -1):
        xk, yk = rc_2[0], rc_2[1]
    else:
        return

    xn += const_x
    xk += const_x

    yn += const_y
    yk += const_y

    parse_methods(xn, yn, xk, yk, option, color)


def parse_methods(xn, yn, xk, yk, option, color, draw = True):
    if (option == 1):
        dots = methods.cda_method(xn, yn, xk, yk, color)
        
        if draw:
            draw_line(dots)

    elif (option == 2):
        dots = methods.bresenham_int(xn, yn, xk, yk, color)

        if draw:
            draw_line(dots)

    elif (option == 3):
        dots = methods.bresenham_float(xn, yn, xk, yk, color)
        
        if draw:
            draw_line(dots)

    elif (option == 4):
        dots = methods.wu(xn, yn, xk, yk, color)
        
        if draw:
            draw_line(dots)

    elif (option == 5):
        dots = methods.bresenham_smooth(xn, yn, xk, yk, color)
        
        if draw:
            draw_line(dots)
    else:
        messagebox.showerror("Ошибка", "Неизвестный алгоритм")


def draw_line(dots):
    for dot in dots:
        col= rgb2hex(dot[2][0], dot[2][1], dot[2][2])
        ui.canv.create_line(dot[0], dot[1], dot[0] + 1, dot[1], fill=col)


def choose_color(color, intens):
    return color + (intens, intens, intens)


def parse_spektr(option, option_color):
    try:
        line_len = float(ui.b_step.get())
        angle_spin = float(ui.b_len.get())
        x = int(ui.b_add_point_entry_xn.get())
        y = int(ui.b_add_point_entry_yn.get())
    except:
        messagebox.showerror("Ошибка", "Неверно введены координаты")
        return

    if (line_len <= 0):
        messagebox.showerror("Ошибка", "Длина линии должна быть выше нуля")
        return

    if (angle_spin <= 0):
        messagebox.showerror("Ошибка", "Угол должен быть больше нуля")
        return

    x += const_x
    y += const_y

    spin = 0

    while (spin <= 2 * pi):
        x2 = x + cos(spin) * line_len
        y2 = y + sin(spin) * line_len

        p2 = [x2, y2]

        parse_methods(x, y, p2[0], p2[1], option, option_color)

        spin += radians(angle_spin)
