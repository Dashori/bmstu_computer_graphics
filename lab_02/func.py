from tkinter import messagebox
from math import sin, cos,pi, radians
import draw

def info_programm():
    messagebox.showinfo("Информация", "Данная программа может поворчавать, перемещать и масштабировать кролика. Чепиго Дарья ИУ7-44Б")

def rotate_point(xc, yc, angle, x, y):
    # x = cos(angle*pi/180)
    # print(x)
    angle = angle*pi/180 
    # x = cos(angle)
    # print(x)
    # print("sin", sin(angle))
    # print("sin", cos(angle))
    # print("sin", sin(radians(angle)))
    print("xc", xc)
    print("x", x)
    print("x - xc", x-xc)
    print("x-xc * cos", (x-xc)*cos(angle))
     
    x1 = xc + (x-xc)*cos(angle) + (y-yc)*sin(angle)
    y1 = yc - (x-xc)*sin(angle) + (y-yc)*cos(angle)
    print(x1, y1)
    print("\n")
   
    return x1, y1

def rotate_rabbit(xc, yc, angle):
    # global contour_rabbit

    for i in range(28):
        print(draw.contour_rabbit[i][0], draw.contour_rabbit[i][1])
        new_coor = rotate_point(xc, yc, angle, draw.contour_rabbit[i][0], draw.contour_rabbit[i][1])
        print(new_coor)
        draw.contour_rabbit[i][0] = new_coor[0]
        draw.contour_rabbit[i][1] = new_coor[1]

        print(" ! ",draw.contour_rabbit[i]) 
    draw.print_rabbit()
    # print(draw.contour_rabbit)    
    