from tkinter import *
from tkinter import messagebox
import ui, main
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

        main.parse_methods(x, y, p2[0], p2[1], option, option_color)

        spin += radians(angle_spin)


def draw_line(dots):
    for dot in dots:
        col= rgb2hex(dot[2][0], dot[2][1], dot[2][2])
        ui.canv.create_line(dot[0], dot[1], dot[0] + 1, dot[1], fill=col)


def draw_pixel(canv, dot):
    col= rgb2hex(dot[2][0], dot[2][1], dot[2][2])
    canv.create_line(dot[0], dot[1], dot[0] + 1, dot[1], fill=col)


def draw_dots_circle(canvas_win, dot_c, dot_dif, color):
    x_c = dot_c[0]
    y_c = dot_c[1]

    x = dot_dif[0]
    y = dot_dif[1]

    draw_pixel(canvas_win, [x_c + x, y_c + y, color])
    draw_pixel(canvas_win, [x_c - x, y_c + y, color])
    draw_pixel(canvas_win, [x_c + x, y_c - y, color])
    draw_pixel(canvas_win, [x_c - x, y_c - y, color])

    draw_pixel(canvas_win, [x_c + y, y_c + x, color])
    draw_pixel(canvas_win, [x_c - y, y_c + x, color])
    draw_pixel(canvas_win, [x_c + y, y_c - x, color])
    draw_pixel(canvas_win, [x_c - y, y_c - x, color])


def draw_dots_ellipse(canvas_win, dot_c, dot_dif, color):
    x_c = dot_c[0]
    y_c = dot_c[1]

    x = dot_dif[0]
    y = dot_dif[1]

    draw_pixel(canvas_win, [x_c + x, y_c + y, color])
    draw_pixel(canvas_win, [x_c - x, y_c + y, color])
    draw_pixel(canvas_win, [x_c + x, y_c - y, color])
    draw_pixel(canvas_win, [x_c - x, y_c - y, color])