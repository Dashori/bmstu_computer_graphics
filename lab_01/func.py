from ctypes import pointer
from math import sqrt
from tkinter import messagebox
import ui_func
import draw

radius = -1
x = 0
y = 0
need_point_1 = []
need_point_2 = []
need_point_3 = []
flag = 0


## функция для нахождения расстояния между двумя точками
def find_distance(point_1, point_2):
    return sqrt((point_1[1]-point_2[1])**2 + (point_1[0]-point_2[0])**2)


##функция для нахождения расстояния до всех других точек
def find_min_distance():
    for i in range(ui_func.count):
        ui_func.min_distance[i] = 0
        for j in range(ui_func.count):
            x = find_distance(ui_func.points[i], ui_func.points[j])
            ui_func.min_distance[i] += x 


## функция для нахождения площади треугольника
def find_square(a,b,c):
    p = (a + b + c)/2
    square = sqrt(p*(p-a)*(p-b)*(p-c))

    return square


## функция для нахождения описанного радиуса треугольника
def find_radius(a,b,c):
    square = find_square(a,b,c)
    r = 0

    if (square != 0):
        r = (a*b*c)/(4*square)
    return r


## функция для нахождения центра описанной окружности
def find_center(x1, y1, x2, y2, x3, y3):
    e = (x2**2 - x1**2) + (y2**2 - y1**2)
    f = (x3**2 - x1**2) + (y3**2 - y1**2)
    g = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)

    global x, y
    x = (y3-y1)*e-(y2-y1)*f
    x /= (2*g)

    y = (x2-x1)*f-(x3-x1)*e
    y /=(2*g)


## функция для нахождения нужной окружности
def find_min_circle():
    if (ui_func.count < 3):
        messagebox.showerror("Ошибка", "Для решения задачи необходимо минимум 3 точки.")
        return
    
    global flag
    flag = 1
        
    find_min_distance()
    min_point = min(ui_func.min_distance)
    index = ui_func.min_distance.index(min_point) 

    ui_func.points[0], ui_func.points[index] = ui_func.points[index],ui_func.points[0]
    ui_func.min_distance[0], ui_func.min_distance[index] = ui_func.min_distance[index], ui_func.min_distance[0] 
    
    global radius
    radius = -1

    global need_point_1, need_point_2, need_point_3
    need_point_1 = ui_func.points[0]

    for i in range(1, ui_func.count - 1):
        for j in range(i + 1, ui_func.count):
            a = find_distance(ui_func.points[0], ui_func.points[i])
            b = find_distance(ui_func.points[0], ui_func.points[j])
            c = find_distance(ui_func.points[i], ui_func.points[j])

            r = find_radius(a,b,c)

            if (r > 0 and (radius == -1 or r < radius)):
                need_point_2 = ui_func.points[i]
                need_point_3 = ui_func.points[j]
                radius = r

    if (radius > 0):
        find_center(need_point_1[0], need_point_1[1], need_point_2[0], need_point_2[1], need_point_3[0], need_point_3[1])

    if (radius == -1):
        messagebox.showerror("Ошибка", "По данным точкам невозможно построить окружность.")
    else:
        draw.scaling_circle()
        draw.print_res_text()

    text = "draw.back_solve()"
    ui_func.back_command.append(text)


## фунция для изменение масштаба по х
def scale_plus():
    draw.text_x = draw.text_x / 1.5
    draw.text_y = draw.text_y / 1.5
    draw.print_points()

    if (draw.flag_canva and radius != -1):
       draw.draw_circle()

    text = "func.scale_minus()"
    ui_func.back_command.append(text)


## фунция для изменение масштаба по у    
def scale_minus():
    draw.text_x = draw.text_x * 1.5
    draw.text_y = draw.text_y * 1.5
    draw.print_points()

    if (draw.flag_canva and radius != -1):
       draw.draw_circle()

    text = "func.scale_plus()"
    ui_func.back_command.append(text)    
    
## функция для округления чисел
def round_numbers(num):
    if (num < 5):
        num = round(num,2)
    else:
        num = int(num)
    return num