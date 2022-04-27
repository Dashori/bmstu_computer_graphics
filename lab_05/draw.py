from gettext import find
from os import POSIX_FADV_RANDOM
from tkinter import *
from tkinter import messagebox
from turtle import color
import pyautogui

import ui, main
from colormap import rgb2hex
from math import pi, cos, sin, radians

const_x = 400
const_y = 350

points = []
edges = []
first_point = None
cur_point = None

pixel_state = []
EPS = 1e-6

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
        return 'a', 'b'

## надфункция для считывания координат из полей ввода    
def add_point_input(input_x, input_y):
    x, y = input_coor(input_x, input_y)

    if (x == 'a' and y == 'b'):
        return

    add_point(x, y)


## функция для проверки номера точки
def check_point(number):
    try:
        index = int(number)
    except:
        messagebox.showerror('Ошибка','Неправильно введён номер точки. Номер точки- целое число.')
        return 1

    global points

    if (len(points) == 0):
        messagebox.showinfo('Информация','Множество точек пусто.')
        return 1

    if (index < 1 or index > len(points)):
        messagebox.showerror('Ошибка','''Неправильно введён номер точки. Номер точки должен быть целым число и не превосходить количество точек множества.''')
        return 1

    return 0
  

## фукция для удаления точки
def del_point(number):
    if (check_point(number) == 1):
        return

    global points

    points.pop(int(number) - 1)

    update_table()
    print_edges()


## функция для обновления таблицы
def update_table():
    ui.tb.config(state='normal')
    ui.tb.delete(0.0, END)
    ui.mytable.clear()

    const = round(ui.width_but/70)
    
    ui.mytable.field_names = [' '*const + '№' + ' '*const, ' '*const + 'X' + ' '*const, ' '*const + 'Y' + ' '*const]

    for i in range(len(points)):
        x = str(round(points[i][0], 2)) 
        y = str(round(points[i][1], 2))
        ui.mytable.add_row([str(i + 1), x, y])

    ui.tb.insert(INSERT, ui.mytable)
    ui.tb.config(state='disable')


## функция для получения координат натыканных точек        
def input_points(event):
    x = float(event.x)
    y = float(event.y)

    add_point(x, y)
    

## функция для добавления точки в таблицу
def add_point(x, y):
    global edges, points
    global cur_point, first_point

    points.append([x, y])

    if cur_point == None or first_point == None:
        cur_point = [x, y]
        first_point = [x, y]
        return

    edges.append([x,y, cur_point[0], cur_point[1]])
    cur_point = [x, y]
    print(" edges ", edges)

    print_edges()
    update_table()


## функция для отрисовки ребер
def print_edges():
    global edges

    ui.canv.delete("all")

    for i in range(len(edges)):
        x1 = edges[i][0]
        y1 = edges[i][1]

        x2 = edges[i][2]
        y2 = edges[i][3]

        ui.canv.create_line(x1, y1, x2, y2)

   
## замкнуть
def lock_edge():
    global edges
    global cur_point, first_point

    try:
        x1 = cur_point[0] 
        y1 = cur_point[1] 

        x2 = first_point[0]
        y2 = first_point[1]
        
        ui.canv.create_line(x1, y1, x2, y2)

        edges.append([x1, y1, x2, y2])

        cur_point = None
        first_point = None
    except:
        messagebox.showerror("Ошибка", "Нечего замыкать.")
        return


## функция для тыканья точек
def input_points_canvas():
    ui.canv.bind('<Button - 1>', input_points)


## функция для очистки всего
def clean():
    ui.canv.delete("all")
    global points, edges
    global cur_point, first_point

    points = []
    edges = []
    cur_point = None
    first_point = None

    ui.tb.config(state='normal')
    ui.tb.delete(0.0, END)
    ui.tb.config(state='disable')


## функция для закрытие окошка
def exit_window(root):
    root.destroy()


## функция для добавления новой точки через поля ввода
def add_point_window():
    add_window=Tk()
    add_window.title('Добавление')
    add_window.geometry('350x150')

    text='Введите координаты точки:'
    input_center_lable=Label(add_window, font='Helvetica 12 bold', text = text, justify=LEFT).place(x=30, y=10)

    input_x_label=Label(add_window, font='Helvetica 12', text='X  =').place(x=30, y=52)
    input_x=Entry(add_window, width=7)
    input_x.place(x=80, y=50)

    input_y_label=Label(add_window, font='Helvetica 12', text='Y  =').place(x=210, y=52)
    input_y=Entry(add_window, width=7)
    input_y.place(x=260, y=50)

    add_button=Button(add_window, font='Helvetica 12', text='Добавить точку', command= lambda:add_point_input(input_x, input_y))
    add_button.place(x=80, y=100)

    exit_button=Button(add_window, font='Helvetica 12', text='Закрыть', command= lambda:exit_window(add_window))
    exit_button.place(x=250, y=100)

    input_x.insert(250,0)
    input_y.insert(250,0)

    add_window.mainloop()

## функция для удаления точки через поля ввода
def del_point_window():
    del_window=Tk()
    del_window.title('Удаление')
    del_window.geometry('300x150')

    text='Введите номер точки:'
    input_center_lable=Label(del_window, font='Helvetica 12 bold', text = text, justify=LEFT).place(x=30, y=10)

    input_num_lab=Label(del_window, font='Helvetica 12', text='N  =').place(x=30, y=52)
    input_num=Entry(del_window, width=7)
    input_num.place(x=80, y=50)

    del_button=Button(del_window, font='Helvetica 12', text='Удалить точку', command= lambda:del_point(input_num.get()))
    del_button.place(x=30, y=100)

    exit_button=Button(del_window, font='Helvetica 12', text='Закрыть', command= lambda:exit_window(del_window))
    exit_button.place(x=180, y=100)

    del_window.mainloop()


## функция для изменения точки через поля ввода
def change_point_window():
    change_window=Tk()
    change_window.title('Изменение')
    change_window.geometry('350x150')

    text='Введите номер точки:'
    input_center_lable=Label(change_window, font='Helvetica 12 bold', text = text, justify=LEFT).place(x=30, y=10)

    input_num=Entry(change_window, width=7)
    input_num.place(x=260, y=10)

    input_x_label=Label(change_window, font='Helvetica 12', text='X  =').place(x=30, y=52)
    input_x=Entry(change_window, width=7)
    input_x.place(x=80, y=50)

    input_y_label=Label(change_window, font='Helvetica 12', text='Y  =').place(x=210, y=52)
    input_y=Entry(change_window, width=7)
    input_y.place(x=260, y=50)
    
    change_button=Button(change_window, font='Helvetica 12', text='Изменить точку')#, command= lambda:del_point(input_num.get()))
    change_button.place(x=80, y=100)

    exit_button=Button(change_window, font='Helvetica 12', text='Закрыть', command= lambda:exit_window(change_window))
    exit_button.place(x=250, y=100)

    change_window.mainloop()



## ищем макс x, min y, max y чтоб докрашивать до правой границы фигуры  
def find_right_edge():
    max_x = points[0][0]
    min_x = points[0][0]
    min_y = points[0][1]
    max_y = points[0][1]

    for i in range(len(points)):
        if (points[i][0] < min_x):
            min_x = points[i][0]
        if (points[i][0] > max_x):
            max_x = points[i][0]
        if (points[i][1] > max_y):
            max_y = points[i][1]
        if (points[i][1] < min_y):
            min_y = points[i][1]

    return int(min_x), int(max_x), int(min_y), int(max_y)

def find_scan_edges(edge):
    if edge[1] > edge[3]:
            edge[1], edge[3] = edge[3], edge[1]
            edge[0], edge[2] = edge[2], edge[0]  

    y = edge[1]
    end_y = edge[3]
    dx = (edge[2] - edge[0]) / (edge[3] - edge[1])
    start_x = edge[0]+ dx

    return y, end_y, dx, start_x

def fill_pixel(x, y, min_x, min_y):
    global pixel_state

    x = int(x)
    y = int(y)

    if (pixel_state[x - min_x][y - min_y] == 0):
        ui.canv.create_oval(x, y, x + 1, y + 1, fill = '#12d9d9', outline = '#12d9d9')
        pixel_state[x - min_x][y - min_y] = 1
    else:
        ui.canv.create_oval(x, y, x + 1, y + 1, fill = '#ffffff', outline = '#ffffff')
        pixel_state[x - min_x][y - min_y] = 0

def fill_edge(edge, min_x, min_y, max_x):
    y, end_y, dx, start_x = find_scan_edges(edge)
    
    while y < end_y:
        x = start_x
        while x < max_x:
            fill_pixel(x, y, min_x, min_y)
            x += 1

        start_x += dx
        y += 1

def pixel_flag(min_x, min_y, max_x, max_y):
    global pixel_state

    print(min_x, max_x, min_y, max_y)

    for i in range(max_x - min_x):
        pixel_state.append([0]*(max_y - min_y))

    for i in range(0, max_x - min_x, 1):
        for j in range(0, max_y - min_y, 1):
            pixel_state[i][j] = 0
        
    # print(pixel_state)

def fill_figure():
    global edges, EPS

    if (len(edges) < 3):
        messagebox.showerror("Ошибка", "Недостаточно ребер для закраски.")
        return
    
    min_x, max_x, min_y, max_y  = find_right_edge()
    pixel_flag(min_x, max_x, min_y, max_y)

    ui.canv.create_line(max_x, min_y, max_x, max_y)

    print(" FILL edges ", edges)

    for i in range (len(edges)):
        if abs(edges[i][1] - edges[i][3]) < EPS: ## горизонт ребро
            continue
        fill_edge(edges[i], min_x, min_y, max_x)
        