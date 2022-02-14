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


def find_distance(point_1, point_2):
    return sqrt((point_1[1]-point_2[1])**2 + (point_1[0]-point_2[0])**2)

def find_min_distance():
    print(ui_func.count)
    for i in range(ui_func.count):
        ui_func.min_distance[i] = 0
        for j in range(ui_func.count):
            x = find_distance(ui_func.points[i], ui_func.points[j])
            ui_func.min_distance[i] += x 
    print(ui_func.min_distance)

def find_square(a,b,c):
    p = (a + b + c)/2
    square = sqrt(p*(p-a)*(p-b)*(p-c))
    
    print("SQUARE", square)
    
    return square

def find_radius(a,b,c):
    square = find_square(a,b,c)
    r = 0
    if (square != 0):
        r = (a*b*c)/(4*square)
    return r

def find_center(x1, y1, x2, y2, x3, y3):

    e = (x2**2 - x1**2) + (y2**2 - y1**2)
    f = (x3**2 - x1**2) + (y3**2 - y1**2)
    g = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)
    global x
    x = (y3-y1)*e-(y2-y1)*f
    x /= (2*g)

    global y
    y = (x2-x1)*f-(x3-x1)*e
    y /=(2*g)

    print(x,y)


def find_min_circle():
   
    if (ui_func.count < 3):
        messagebox.showerror("Ошибка", "Для решения задачи необходимо минимум 3 точки.")
        return
    find_min_distance()
    min_point = min(ui_func.min_distance)
    print(min_point)
    index = ui_func.min_distance.index(min_point) 

    print("POINTS ",ui_func.points)
    print("Min distance", ui_func.min_distance)

    ## для удобства ставим на 1 место точку, которая точно будет в окружности

    ui_func.points[0], ui_func.points[index] = ui_func.points[index],ui_func.points[0]

    ui_func.min_distance[0], ui_func.min_distance[index] = ui_func.min_distance[index], ui_func.min_distance[0] 

    print("POINTS ",ui_func.points)
    print("Min distance", ui_func.min_distance)

    global radius
    radius = -1

    global need_point_1, need_point_2, need_point_3
    need_point_1 = ui_func.points[0]

    for i in range(1, ui_func.count):
        for j in range(i + 1, ui_func.count):
            a = find_distance(ui_func.points[0], ui_func.points[i])
            b = find_distance(ui_func.points[0], ui_func.points[j])
            c = find_distance(ui_func.points[i], ui_func.points[j])
            print("точки", ui_func.points[0], ui_func.points[i], ui_func.points[j])

            print("стороны ",a,b,c)
            r = find_radius(a,b,c)
            print(r)
            print("\n")
            if (r > 0 and (radius == -1 or r < radius)):
                need_point_2 = ui_func.points[i]
                need_point_3 = ui_func.points[j]
                radius = r

    if (radius > 0):
        find_center(need_point_1[0], need_point_1[1], need_point_2[0], need_point_2[1], need_point_3[0], need_point_3[1])
        global x, y
        print("Center ", x, y)

    print("Radius", radius)
    if (radius == -1):
        messagebox.showerror("Ошибка", "По данным точкам невозможно построить окружность.")
    else:
       draw.draw_circle()

        