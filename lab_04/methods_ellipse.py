from math import pi, cos, sin, sqrt
import draw


def parametric_ellips(canvas_win, dot_c, rad, color, draw_flag):
    x_c = dot_c[0]
    y_c = dot_c[1]

    if (rad[0] > rad[1]):
        step = 1 / rad[0]
    else:
        step = 1 / rad[1]

    alpha = 0

    while (alpha < pi / 2 + step):
        x = round(rad[0] * cos(alpha))
        y = round(rad[1] * sin(alpha))

        if draw_flag:
            draw.draw_dots_ellipse(canvas_win, [x_c, y_c], [x, y], color)

        alpha += step


def mid_dot_ellipse(canvas_win, dot_c, rad, color, draw_flag):
    x_c = dot_c[0]
    y_c = dot_c[1]

    x = 0
    y = rad[1]

    r_a_2 = rad[0] * rad[0]
    r_b_2 = rad[1] * rad[1]

    edge = round(rad[0] / sqrt(1 + r_b_2 / r_a_2))
    delta = r_b_2 - round(r_a_2 * (rad[1] - 1 / 4))

    while (x <= edge):
        if draw_flag:
            draw.draw_dots_ellipse(canvas_win, [x_c, y_c], [x, y], color)

        if (delta > 0):
            y -= 1
            delta = delta - r_a_2 * y * 2

        x += 1
        delta = delta + r_b_2 * (2 * x + 1)

    x = rad[0]
    y = 0

    r_a_2 = rad[0] * rad[0]
    r_b_2 = rad[1] * rad[1]

    edge = round(rad[1] / sqrt(1 + r_a_2 / r_b_2))
    delta = r_a_2 - round(r_b_2 * (x - 1 / 4))

    while (y <= edge):
        if draw_flag:
            draw.draw_dots_ellipse(canvas_win, [x_c, y_c], [x, y], color)

        if (delta > 0):
            x -= 1
            delta = delta - r_b_2 * x * 2

        y += 1
        delta = delta + r_a_2 * (2 * y + 1)


def canon_ellips(canvas_win, dot_c, rad, color, draw_flag):
    x_c = dot_c[0]
    y_c = dot_c[1]

    r_a = rad[0]
    r_b = rad[1]

    double_ra = r_a * r_a
    double_rb = r_b * r_b

    edge = round(double_ra / sqrt(double_ra + double_rb))
    x = 0

    while (x <= edge):
        y = round(sqrt(1 - x * x / double_ra) * r_b)

        if draw_flag:
            draw.draw_dots_ellipse(canvas_win, [x_c, y_c], [x, y], color)

        x += 1

    edge = round(double_rb / sqrt(double_ra + double_rb))
    y = 0

    while (y <= edge):
        x = round(sqrt(1 - y * y / double_rb) * r_a)

        if draw_flag:   
            draw.draw_dots_ellipse(canvas_win, [x_c, y_c], [x, y], color)

        y += 1
    

def bresenham_ellipse(canvas_win, dot_c, rad, color, draw_flag):
    x_c = round(dot_c[0])
    y_c = round(dot_c[1])

    x = 0
    y = rad[1]

    r_a_2 = rad[0] * rad[0]
    r_b_2 = rad[1] * rad[1]

    delta_i = r_b_2 - r_a_2 * (2 * y + 1)
    eps = 0

    while (y >= 0):

        if draw_flag:
            draw.draw_dots_ellipse(canvas_win, [x_c, y_c], [x, y], color)

        if (delta_i <= 0):
            eps = 2 * delta_i + (2 * y + 2) * r_a_2

            if (eps < 0):
                param = 1
            else:
                param = 2
        elif (delta_i > 0):
            eps = 2 * delta_i + (- 2 * x + 2) * r_b_2

            if (eps < 0):
                param = 2
            else:
                param = 3
        
        if (param == 1):
            x = x + 1
            delta_i = delta_i + (2 * x) * r_b_2 + r_b_2
        elif (param == 2):
            x = x + 1
            y = y - 1
            delta_i = delta_i + (2 * x) * r_b_2 - (2 * y) * r_a_2 + (r_a_2 + r_b_2)
        else:
            y = y - 1
            delta_i = delta_i - (2 * y) * r_a_2 + r_a_2

