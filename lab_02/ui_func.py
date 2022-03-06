from tkinter import *
from tkinter import messagebox
from math import sin, cos, pi
import ui, draw

back_command = []

## функция для считывания координа х и у из полей ввода
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
    button.config(state='normal')


## функция для изменения координат точки во время поворота
def rotate_point(xc, yc, angle, x, y):
    angle = angle*pi/180 
     
    x1 = xc + (x-xc)*cos(angle) + (y-yc)*sin(angle)
    y1 = yc - (x-xc)*sin(angle) + (y-yc)*cos(angle)

    return x1, y1


## функция для вращения кролика
def rotate_rabbit(xc, yc, angle):
    for i in range(len(draw.contour_rabbit)):
        new_coor = rotate_point(xc, yc, angle, draw.contour_rabbit[i][0], draw.contour_rabbit[i][1])
        draw.contour_rabbit[i][0] = new_coor[0]
        draw.contour_rabbit[i][1] = new_coor[1]

    text="rotate_rabbit(" + str(xc) + "," + str(yc) + "," + str((-1)*angle) + ")"
    back_command.append(text)

    draw.print_rabbit(xc,yc)


## функция функция для считывания угла и центра поворота
def input_rotate(input_angle_entry, input_x, input_y):
    angle=input_angle(input_angle_entry)
    center=input_coor(input_x, input_y)

    if (angle == None or center == None):
        return

    x,y = center[0] + draw.const_x - draw.center_x, -center[1] + draw.const_y - draw.center_y
    rotate_rabbit(x, y, angle)


## функция для обработки введённого угла
def input_angle(input_angle_entry):
    try:
        angle=float(input_angle_entry.get())
    except:
        messagebox.showerror("Ошибка","Неправильно ввёден угол поворота")
        input_angle_entry.delete(0,'end')
        return
    return angle


## функция для отображения окна и вращения изображения
def rotate_window():
    window_rotate=Tk()
    window_rotate.title('Поворот')
    window_rotate.geometry('350x200')

    input_angle_lable=Label(window_rotate, font='Helvetica 12 bold', text = 'Введите угол поворота:').place(x=30, y=30)
   
    input_angle_entry=Entry(window_rotate, width=7)
    input_angle_entry.place(x=240, y=27)

    text='Введите точку,относительно\n\
которой поворачивать кролика:'
    input_coord_lable=Label(window_rotate, font='Helvetica 12 bold', text = text, justify=LEFT).place(x=30, y=70)

    input_x_label=Label(window_rotate, font='Helvetica 12', text='X =').place(x=30, y=125)
    input_x=Entry(window_rotate, width=7)
    input_x.place(x=65, y=122)

    input_y_label=Label(window_rotate, font='Helvetica 12', text='Y =').place(x=210, y=125)
    input_y=Entry(window_rotate, width=7)
    input_y.place(x=240, y=122)

    rotate_button=Button(window_rotate, font='Helvetica 12', text='Повернуть', command= lambda:input_rotate(input_angle_entry, input_x, input_y))
    rotate_button.place(x=140, y=155)

    exit_button=Button(window_rotate, font='Helvetica 12', text='Закрыть', command= lambda:exit_window(window_rotate, ui.rotate_button_main))
    exit_button.place(x=250, y=155)

    input_x.insert(0,0)
    input_y.insert(0,0)
    input_angle_entry.insert(0,10)

    window_rotate.attributes("-topmost", True)
    window_rotate.mainloop()


## функция для изменения координат кролика во время перемещения
def move_rabbit(x, y):
    for i in range(len(draw.contour_rabbit)):
        draw.contour_rabbit[i][0] += x
        draw.contour_rabbit[i][1] += y


    text="move_rabbit(" + str(-x) + "," + str(-y) + ")"
    back_command.append(text)

    draw.print_rabbit()


## функция для обработки введённых координат перемещения
def input_transfer_count(input_x, input_y):
    center=input_coor(input_x, input_y)

    if (center == None):
        return

    x,y = center[0], -center[1]
    move_rabbit(x, y)


## функция для появления окошка и перемещения изображения
def move_window():
    window_move=Tk()
    window_move.title('Перемещение')
    window_move.geometry('350x200')

    text='Введите смещение кролика:'
    input_coord_lable=Label(window_move, font='Helvetica 12 bold', text = text, justify=LEFT).place(x=30, y=30)

    input_x_label=Label(window_move, font='Helvetica 12', text='X  =').place(x=30, y=70)
    input_x=Entry(window_move, width=7)
    input_x.place(x=80, y=65)

    input_y_label=Label(window_move, font='Helvetica 12', text='Y  =').place(x=210, y=70)
    input_y=Entry(window_move, width=7)
    input_y.place(x=260, y=65)

    rotate_button=Button(window_move, font='Helvetica 12', text='Переместить', command= lambda:input_transfer_count(input_x, input_y))
    rotate_button.place(x=120, y=130)

    exit_button=Button(window_move, font='Helvetica 12', text='Закрыть', command= lambda:exit_window(window_move, ui.transfer_button))
    exit_button.place(x=250, y=130)

    input_x.insert(0,50)
    input_y.insert(0,50)

    window_move.attributes("-topmost", True)

    window_move.mainloop()


## функция для изменения координат при масштабировании
def scale_rabbit(xc, yc, kx, ky):
    for i in range(len(draw.contour_rabbit)):
        draw.contour_rabbit[i][0] = xc + kx*(draw.contour_rabbit[i][0]-xc)
        draw.contour_rabbit[i][1] = yc + ky*(draw.contour_rabbit[i][1]-yc)

    draw.print_rabbit()


## функция для обработки параметров для масштабирования
def input_scale_coor(input_xc, input_yc, input_kx, input_ky):
    center=input_coor(input_xc, input_yc)
    ratio=input_coor(input_kx, input_ky)    

    if (center==None or ratio==None):
        return

    xc, yc=center[0] + draw.const_x - draw.center_x, draw.const_y - draw.center_y -center[1]
    kx, ky=ratio[0], ratio[1]
    scale_rabbit(xc, yc, kx, ky)


## функция для появления окошка и масштабирования
def scale_window():
    window_scale=Tk()
    window_scale.title('Масштабирование')
    window_scale.geometry('350x250')

    text='Введите точку,относительно\n\
которой масштабировать кролика:'
    input_center_lable=Label(window_scale, font='Helvetica 12 bold', text = text, justify=LEFT).place(x=30, y=10)

    input_x_center_label=Label(window_scale, font='Helvetica 12', text='X  =').place(x=30, y=65)
    input_x_center=Entry(window_scale, width=7)
    input_x_center.place(x=80, y=65)

    input_y_center_label=Label(window_scale, font='Helvetica 12', text='Y  =').place(x=210, y=65)
    input_y_center=Entry(window_scale, width=7)
    input_y_center.place(x=260, y=65)

    text='Введите коэфициенты\n\
масштабирования:'
    input_coord_lable=Label(window_scale, font='Helvetica 12 bold', text = text, justify=LEFT).place(x=30, y=110)

    input_x_label=Label(window_scale, font='Helvetica 12', text='X  =').place(x=30, y=155)
    input_kx=Entry(window_scale, width=7)
    input_kx.place(x=80, y=152)

    input_y_label=Label(window_scale, font='Helvetica 12', text='Y  =').place(x=210, y=155)
    input_ky=Entry(window_scale, width=7)
    input_ky.place(x=260, y=152)

    rotate_button=Button(window_scale, font='Helvetica 12', text='Изменить масштаб', command= lambda:input_scale_coor(input_x_center, input_y_center, input_kx, input_ky))
    rotate_button.place(x=80, y=200)

    exit_button=Button(window_scale, font='Helvetica 12', text='Закрыть', command= lambda:exit_window(window_scale, ui.scale_button))
    exit_button.place(x=250, y=200)

    input_x_center.insert(0,0)
    input_y_center.insert(0,0)

    input_kx.insert(0,2)
    input_ky.insert(0,2)

    window_scale.attributes("-topmost", True)
    window_scale.mainloop()
    
def back():
    global back_command

    if (len(back_command) == 0):
        messagebox.showinfo("Информация", "Вы выполнили все обратные действия.")
        return

    eval(back_command[len(back_command) - 1])
    back_command.pop(len(back_command) - 1)
    back_command.pop(len(back_command) - 1)