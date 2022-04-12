import ui, draw, methods
from tkinter import messagebox
import time, numpy
from math import pi, cos, sin, radians
import matplotlib.pyplot as plt

def time_measure():

    time_mes = []

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

    x += draw.const_x
    y += draw.const_y

    for i in range(1, 6):
        res_time = 0

        for _ in range(500):
            time_start = 0
            time_end = 0

            spin = 0

            while (spin <= 2 * pi):
                x2 = x + cos(spin) * line_len
                y2 = y + sin(spin) * line_len

                time_start += time.time()
                draw.parse_methods(x, y, x2, y2, i, ui.const_draw, draw = False)
                time_end += time.time()

                spin += radians(angle_spin)

            res_time += (time_end - time_start)

            ui.canv.delete("all")


        time_mes.append(res_time / 20)


    plt.figure(figsize = (14, 5))
    plt.title("Замеры времени для различных методов")

    positions = numpy.arange(5)
    methods = ["ЦДА", "Брезенхем (float)", "Брезенхем (int)", "Ву", "Брезенхем (сглаживание)"]

    plt.xticks(positions, methods)
    plt.ylabel("Время")
    plt.bar(positions, time_mes, align = "center", alpha = 1)
    plt.show()


def steps_measure():
    try:
        line_len = line_len = float(ui.b_step.get())
        x = int(ui.b_add_point_entry_xn.get())
        y = int(ui.b_add_point_entry_yn.get())
    except:
        messagebox.showerror("Ошибка", "Неверно введены координаты")
        return

    if (line_len <= 0):
        messagebox.showerror("Ошибка", "Длина линии должна быть выше нуля")
        return

    x += draw.const_x
    y += draw.const_y

    spin = 0

    angle_spin = [i for i in range(0, 91, 2)]
    cda_steps = []
    wu_steps = []
    bres_int_steps = []
    bres_float_steps = []
    bres_smooth_steps = []

    while (spin <= pi / 2 + 0.01):
        x2 =  x + cos(spin) * line_len
        y2 =  y + sin(spin) * line_len

        
        cda_steps.append(methods.cda_method(x, y, x2, y2, (255, 255, 255), step_count = True))
        wu_steps.append(methods.wu(x, y, x2, y2, (255, 255, 255), step_count = True))
        bres_int_steps.append(methods.bresenham_int(x, y, x2, y2, (255, 255, 255), step_count = True))
        bres_float_steps.append(methods.bresenham_float(x, y, x2, y2, (255, 255, 255), step_count = True))
        bres_smooth_steps.append(methods.bresenham_smooth(x, y, x2, y2, (255, 255, 255), step_count = True))

        spin += radians(2)


    plt.figure(figsize = (15, 6))
    plt.title("Замеры ступенчатости для различных методов\n{0} - длина отрезка".format(line_len))
    plt.xlabel("Угол (в градусах)")
    plt.ylabel("Количество ступенек")

    plt.plot(angle_spin, cda_steps, label = "ЦДА")
    plt.plot(angle_spin, wu_steps, label = "Ву")
    plt.plot(angle_spin, bres_float_steps, "-.", label = "Брезенхем (float/int)")
    plt.plot(angle_spin, bres_smooth_steps, ":", label = "Брезенхем\n(сглаживание)")

    plt.xticks(numpy.arange(91, step = 5))

    plt.legend()
    plt.show()