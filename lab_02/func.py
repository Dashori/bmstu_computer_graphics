from tkinter import messagebox
from math import sin, cos,pi, radians
import draw

def info_programm():
    messagebox.showinfo("Информация", "Данная программа может поворчавать, перемещать и масштабировать кролика. Чепиго Дарья ИУ7-44Б")

def rotate_point(xc, yc, angle, x, y):
    angle = angle*pi/180 
     
    x1 = xc + (x-xc)*cos(angle) + (y-yc)*sin(angle)
    y1 = yc - (x-xc)*sin(angle) + (y-yc)*cos(angle)

    return x1, y1

def rotate_rabbit(xc, yc, angle):
    for i in range(len(draw.contour_rabbit)):
        new_coor = rotate_point(xc, yc, angle, draw.contour_rabbit[i][0], draw.contour_rabbit[i][1])
        draw.contour_rabbit[i][0] = new_coor[0]
        draw.contour_rabbit[i][1] = new_coor[1]

    draw.print_rabbit(xc,yc)

## функция для округления чисел
def round_numbers(num):
    if (num < 5):
        num = round(num,2)
    else:
        num = int(num)
    return num