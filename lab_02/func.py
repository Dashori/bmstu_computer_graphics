from tkinter import messagebox
from math import sin, cos, pi, radians
import draw

def info_programm():
    messagebox.showinfo("Информация", "Данная программа может поворчавать, перемещать и масштабировать кролика. Чепиго Дарья ИУ7-44Б")

def rotate_point(x, y, angle):
    # x = cos(angle*pi/180)
    # print(x)
    angle = radians(angle) 
    # x = cos(angle)
    # print(x)
    
    x = x*cos(angle) - y*sin(angle)
    y = x*sin(angle) + y*cos(angle)  
    return x, y

def rotate_rabbit(angle):

    for i in range(len(draw.contour_rabbit) - 1):
        new_coor = rotate_point(draw.contour_rabbit[i][0], draw.contour_rabbit[i][1], angle)
        draw.contour_rabbit[i][0] = new_coor[0]
        draw.contour_rabbit[i][0] = new_coor[1]
     
    draw.print_rabbit()
    
    