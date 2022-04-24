from math import pi, cos, sin, sqrt
import draw, ui
from colormap import rgb2hex


def lib_method(dot_c, rad, color):
    col= rgb2hex(color[0], color[1], color[2])
    ui.canv.create_oval(dot_c[0] - rad[0], dot_c[1] - rad[1], dot_c[0] + rad[0], dot_c[1] + rad[1], outline=col) 
    

def parametric_circle(canvas_win, dot_c, radius, color, draw_flag):
    x_c = dot_c[0]
    y_c = dot_c[1]

    step = 1 / radius
    alpha = 0

    while (alpha < pi / 4 + step):
        x = round(radius * cos(alpha))
        y = round(radius * sin(alpha))

        if draw_flag:
            draw.draw_dots_circle(canvas_win, [x_c, y_c], [x, y], color)

        alpha += step


def mid_dot_circle(canvas_win, dot_c, radius, color, draw_flag):
    x_c = dot_c[0]
    y_c = dot_c[1]

    x = 0
    y = radius
    delta = 1 - radius

    while (x <= y):
        if draw_flag:
            draw.draw_dots_circle(canvas_win, [x_c, y_c], [x, y], color)

        x += 1

        if (delta < 0):
            delta = delta + 2 * x + 1
        else:
            y -= 1
            delta = delta + 2 * (x - y) + 1


def canon_circle(canvas_win, dot_c, radius, color, draw_flag):
    x_c = dot_c[0]
    y_c = dot_c[1]

    edge = round(radius / sqrt(2))
    double_radius = radius * radius
    x = 0

    while (x <= edge):
        y = round(sqrt(double_radius - x * x))

        if draw_flag:
            draw.draw_dots_circle(canvas_win, [x_c, y_c], [x, y], color)

        x += 1


def bresenham_circle(canvas_win, dot_c, radius, color, draw_flag):
    x_c = round(dot_c[0])
    y_c = round(dot_c[1])

    x = 0
    y = radius

    delta_i = 2 * (1 - radius)
    eps = 0

    while (x <= y):
        if draw_flag:
            draw.draw_dots_circle(canvas_win, [x_c, y_c], [x, y], color)

        if (delta_i <= 0):
            eps = 2 * delta_i + 2 * y - 1

            if (eps < 0):
                param = 1
            else:
                param = 2
        elif (delta_i > 0):
            eps = 2 * delta_i - 2 * x - 1

            if (eps < 0):
                param = 2
            else:
                param = 3

        if (param == 1):
            x = x + 1
            delta_i = delta_i + 2 * x + 1
        elif (param == 2):
            x = x + 1
            y = y - 1
            delta_i = delta_i + 2 * x - 2 * y + 2
        else:
            y = y - 1
            delta_i = delta_i - 2 * y + 1
