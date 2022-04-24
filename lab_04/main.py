from tkinter import *
from tkinter import messagebox, colorchooser
import ui, methods_circle, methods_ellipse

def task_programm():
    messagebox.showinfo("Информация",
'''Данная программа реализует и исследует
алгоритмы построения окружностей и эллипсов.

Алгоритмы: 
- Канонического уравнения
- Параметрического уравнения
- Алгоритма Брезенхема 
- Алгоритма средней точки
- Библиотечна функция''')


def info_programm():
    messagebox.showinfo("Информация","Лабораторна работа №4. Чепиго Дарья ИУ7-44Б")


## функция для считывания координат х и у из полей ввода
def input_coor(input_x, input_y):
    x=input_x.get()
    y=input_y.get()

    try:
        x=float(input_x.get())
        y=float(input_y.get())
        return x,y
    except:
        messagebox.showerror("Ошибка","Неправильно ввёдены числовые значения.")
        input_x.delete(0,'end')
        input_y.delete(0,'end')
        return 


## функция для закрытие окошка и возврата кнопки в состояние нормал
def exit_window(root, button):
    root.destroy()


def change_window_canv():
    ui.canv.config(bg=ui.const_bg[1])


def change_bg():
    ui.const_bg = colorchooser.askcolor()
    change_window_canv()


def change_draw():
    a = colorchooser.askcolor()
    ui.const_draw = a[0]
    


def parse_spektr_circle(option, option_color, option_figure, option_spektr_crcl):
    # Choose combination

    try:
        x = float(ui.add_point_entry_xc.get())
        y = float(ui.add_point_entry_yc.get())
    except:
        messagebox.showerror("Ошибка", "Неверно введены координаты центра")
        return


    if (option_spektr_crcl == 1):
        try:
            amount = int(ui.count.get())
            rad_begin = float(ui.spectrum_radius_start_entry.get())
            rad_end = float(ui.spectrum_radius_end_entry.get())
        except:
            messagebox.showerror("Ошибка", "Неверно введены координаты")
            return
        rad_step = int((rad_end - rad_begin) / amount)
    elif (option_spektr_crcl == 2):
        try:
            rad_step = float(ui.step.get())
            rad_begin = float(ui.spectrum_radius_start_entry.get())
            rad_end = float(ui.spectrum_radius_end_entry.get())
        except:
            messagebox.showerror("Ошибка", "Неверно введены координаты")
            return
        amount = int((rad_end - rad_begin) / rad_step)
    elif (option_spektr_crcl == 3):
        try:
            amount = int(ui.count.get())
            rad_step = float(ui.step.get())
            rad_end = float(ui.spectrum_radius_end_entry.get())
        except:
            messagebox.showerror("Ошибка", "Неверно введены координаты")
            return
        rad_begin = float(rad_end - rad_step * amount)
    elif (option_spektr_crcl == 4):
        try:
            amount = int(ui.count.get())
            rad_step = float(ui.step.get())
            rad_begin = float(ui.spectrum_radius_start_entry.get())
        except:
            messagebox.showerror("Ошибка", "Неверно введены координаты")
            return
        rad_end = float(rad_begin + rad_step * amount)

    if (rad_begin > rad_end):
        messagebox.showerror("Ошибка", "Начальный радиус не может быть больше конечного")
        return

    if (rad_step <= 0):
        messagebox.showerror("Ошибка", "Шаг радиуса должен быть выше нуля")
        return

    if (amount <= 0):
        messagebox.showerror("Ошибка", "Количество должно быть больше нуля")
        return

    r_a = rad_begin
    r_b = rad_begin

    dot_c = [x, y]

    index = 0

    while (index < amount):
        rad = [r_a, r_b]

        parse_methods(dot_c, rad, option, option_color, option_figure)

        r_a += rad_step
        r_b += rad_step
        
        index += 1


def parse_figure(option, option_color, option_figure):
    try:
        x_c = float(ui.add_point_entry_xc.get())
        y_c = float(ui.add_point_entry_yc.get())

        if (option_figure == 1):
            r_a = float(ui.radius_entry.get())
            r_b = r_a
        else:
            r_a = float(ui.radius_1_entry.get())
            r_b = float(ui.radius_2_entry.get())
    except:
        messagebox.showerror("Ошибка", "Неверно введены координаты")
        return

    dot_c = [x_c, y_c]
    rad = [r_a, r_b]

    parse_methods(dot_c, rad, option, option_color, option_figure)

def parse_spektr_ellips(option, option_color, option_figure):
    try:
        rad_step = float(ui.step.get())
        amount = int(ui.count.get())

        r_a = float(ui.spectrum_radius_1_entry.get())
        r_b = float(ui.spectrum_radius_2_entry.get())

        x = float(ui.add_point_entry_xc.get())
        y = float(ui.add_point_entry_yc.get())
    except:
        messagebox.showerror("Ошибка", "Неверно введены координаты")
        return

    if (rad_step <= 0):
        messagebox.showerror("Ошибка", "Шаг радиуса должен быть выше нуля")
        return

    if (amount <= 0):
        messagebox.showerror("Ошибка", "Количество должно быть больше нуля")
        return

    dot_c = [x, y]
    index = 0
    koef = r_b / r_a

    while (index < amount):
        rad = [r_a, r_b]

        parse_methods(dot_c, rad, option, option_color, option_figure)

        r_a += rad_step
        r_b = (r_a * koef)
        
        index += 1


def choose_spektr(option, option_color, option_figure, option_spektr_crcl):
    if (option_figure == 1):
        parse_spektr_circle(option, option_color, option_figure, option_spektr_crcl)
    elif (option_figure == 2):
        parse_spektr_ellips(option, option_color, option_figure)



def parse_methods(dot_c, rad, option, option_color, option_figure, draw = True):
    color = option_color

    if (option == 1): # canon
        if (option_figure == 1):
            methods_circle.canon_circle(ui.canv, dot_c, rad[0], color, draw)
        elif (option_figure == 2):
            methods_ellipse.canon_ellips(ui.canv, dot_c, rad, color, draw)

    elif (option == 2): # param
        if (option_figure == 1):
            methods_circle.parametric_circle(ui.canv, dot_c, rad[0], color, draw)
        elif (option_figure == 2):
            methods_ellipse.parametric_ellips(ui.canv, dot_c, rad, color, draw)

    elif (option == 3): # bres
        if (option_figure == 1):
            methods_circle.bresenham_circle(ui.canv, dot_c, rad[0], color, draw)
        elif (option_figure == 2):
            methods_ellipse.bresenham_ellipse(ui.canv, dot_c, rad, color, draw)
        

    elif (option == 4): # mid point
        if (option_figure == 1):
            methods_circle.mid_dot_circle(ui.canv, dot_c, rad[0], color, draw)
        elif (option_figure == 2):
            methods_ellipse.mid_dot_ellipse(ui.canv, dot_c, rad, color, draw)
        

    elif (option == 5):
        methods_circle.lib_method(dot_c, rad, color)

