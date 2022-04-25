from tkinter import *
from tkinter import messagebox
import ui, main
from colormap import rgb2hex
from math import pi, cos, sin, radians

const_x = 400
const_y = 350

points = []

## функция для считывания координат х и у из полей ввода
def input_coor(input_x, input_y):
    x = input_x.get()
    y = input_y.get()

    try:
        x = float(input_x.get())
        y = float(input_y.get())
        return x, y
    except:
        messagebox.showerror("Ошибка", "Неправильно ввёдены числовые значения.")
        input_x.delete(0, "end")
        input_y.delete(0, "end")
        

## функция для обновления таблицы
def update_table():
    ui.tb.config(state='normal')
    ui.tb.delete(0.0, END)
    ui.mytable.clear()

    const = round(30/6)
    
    ui.mytable.field_names = [' '*const + '№' + ' '*const, ' '*const + 'X' + ' '*const, ' '*const + 'Y' + ' '*const]

    for i in range(len(points)):
        x = str(round(points[i][0], 2)) 
        y = str(round(points[i][1], 2))
        ui.mytable.add_row([str(i + 1), x, y])

    ui.tb.insert(INSERT, ui.mytable)
    ui.tb.config(state='disable')

## функция для получения координат натыканных точек        
def input_points(event):
    x = event.x
    y = event.y

    print(x, y)

    x = float(x) # - const_x) * text_x / const_x 
    y = float(y)# - const_y) * text_y / const_y

    add_point(x, y)
    

## функция для добавления точки в таблицу
def add_point(x, y):

    points.append([x,y])

    # update_table()

    print_edges()
    update_table()

## функция для отрисовки ребер
def print_edges():
    ui.canv.delete("all")

    for i in range(len(points) - 1):
        x_1 = points[i][0] 
        y_1 = points[i][1]

        x_2 = points[i + 1][0] 
        y_2 = points[i + 1][1]

        ui.canv.create_line(x_1, y_1, x_2, y_2)

## замкнуть
def lock_edge():
    try:
        x_1 = points[0][0] 
        y_1 = points[0][1]

        x_2 = points[len(points) - 1][0] 
        y_2 = points[len(points) - 1][1]

        ui.canv.create_line(x_1, y_1, x_2, y_2)
    except:
        messagebox.showerror("Ошибка", "Нечего замыкать.")
        return


def draw_line(dots):
    for dot in dots:
        col= rgb2hex(dot[2][0], dot[2][1], dot[2][2])
        ui.canv.create_line(dot[0], dot[1], dot[0] + 1, dot[1], fill=col)

def choose_color(color, intens):
    return color + (intens, intens, intens)


def draw_line(dots):
    for dot in dots:
        col= rgb2hex(dot[2][0], dot[2][1], dot[2][2])
        ui.canv.create_line(dot[0], dot[1], dot[0] + 1, dot[1], fill=col)


def draw_pixel(canv, dot):
    col= rgb2hex(dot[2][0], dot[2][1], dot[2][2])
    canv.create_line(dot[0], dot[1], dot[0] + 1, dot[1], fill=col)


## функция для тыканья точек
def input_points_canvas():
    ui.canv.bind('<Button - 1>', input_points)


## функция для очистки всего
def clean():
    ui.canv.delete("all")
    global points
    points=[]

    ui.tb.config(state='normal')
    ui.tb.delete(0.0, END)
    ui.tb.config(state='disable')
    

## ищем макс x, min y, max y чтоб докрашивать до правой границы фигуры  
def find_right_edge():
    max_x = points[0][0]
    min_y = points[0][1]
    max_y = points[0][1]

    for i in range(len(points)):
        if (points[i][0] > max_x):
            max_x = points[i][0]
        if (points[i][1] > max_y):
            max_y = points[i][1]
        if (points[i][1] < min_y):
            min_y = points[1][1]

    return max_x, min_y, max_y


def fill_figure():
    global points

    if (len(points) < 3):
        messagebox.showerror("Ошибка", "Недостаточно ребер для закраски.")
        return
    
    max_x, min_y, max_y  = find_right_edge()

    print(max_x, min_y, max_y)
    ui.canv.create_line(max_x, min_y, max_x, max_y)


