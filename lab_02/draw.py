from tkinter import *
from tkinter import messagebox

import ui
import func

contour_rabbit=[[194, 178], [75, 147], [30, 98], [102, 104], [156, 117], [110, 88],
[93, 29], [166, 60], [269, 140], [336, 175], [346, 206], [279, 254], [262, 304],
[295, 358], [262, 348], [283, 394], [236, 366], [220, 383], [281, 416], [220, 416],
[277, 450], [154, 450], [90, 400], [83, 343], [42, 341],
[34, 290], [65, 280], [82, 298], [206, 236],
[207, 164], [214, 127], [273, 182], [198, 404], [61, 312], [252, 329]]

# contour_rabbit=[[100, 100],[200, 300],[300, 100]]

inside_rabbit= [[2, 4], [6, 8], [4, 30], [5, 31], [6, 31], [8, 31], [9, 31],
[9, 30], [1, 30], [32, 9], [32, 10], [32, 12], [32, 29], [35, 12], [10, 12],
[29,12], [29, 15], [29, 17], [29, 23], [23, 17], [22, 33], [33, 17], [20, 33],
[34, 24], [34, 25], [34, 26], [34, 27], [34, 28], [24, 28]] ##хвост

# center_x =  180 
# center_y = 50
center_x = 0 
center_y = 0

def print_rabbit():
    global contour_rabbit
    ui.canv.delete("all")
    for i in range(28):
        x1 = contour_rabbit[i][0] + center_x
        y1 = contour_rabbit[i][1] + center_y

        x2 = contour_rabbit[i+1][0] + center_x
        y2 = contour_rabbit[i+1][1] + center_y
        ui.canv.create_line(x1, y1, x2, y2, width=4)

    print(" 1",contour_rabbit)

    # ui.canv.create_line(contour_rabbit[0][0] + center_x, contour_rabbit[0][1] + center_y,
    # contour_rabbit[28][0] + center_x, contour_rabbit[28][1] + center_y, width=4)

    # for i in range(len(inside_rabbit)):
    #     x1 = contour_rabbit[inside_rabbit[i][0] - 1][0] + center_x
    #     y1 = contour_rabbit[inside_rabbit[i][0] - 1][1] + center_y

    #     x2 = contour_rabbit[inside_rabbit[i][1] - 1][0] + center_x
    #     y2 = contour_rabbit[inside_rabbit[i][1] - 1][1] + center_y

    #     ui.canv.create_line(x1, y1, x2, y2, width=2)

    ui.canv.create_oval(200, 200, 205, 205)

def input_rotate(input_angle_entry, input_x, input_y):
    angle=input_angle(input_angle_entry)
    center= input_center(input_x, input_y)

    if (angle == None or center == None):
        return

    x, y=center[0], center[1]
    print("x,y", x, y)
    print("angle =", angle)
    func.rotate_rabbit(x, y, angle)


def input_angle(input_angle_entry):
    try:
        angle=float(input_angle_entry.get())
    except:
        messagebox.showerror("Ошибка","Неправильно ввёден угол поворота")
        input_angle_entry.delete(0,'end')
        return
    return angle


def input_center(input_x, input_y):
    x=input_x.get()
    y=input_y.get()

    try:
        x=float(input_x.get())
        y=float(input_y.get())
        return x,y
    except:
        messagebox.showerror("Ошибка","Неправильно ввёден центр поворота")
        input_x.delete(0,'end')
        input_y.delete(0,'end')
        return 


def rotate_window():

    window_rotate=Tk()
    window_rotate.title('Поворот')
    window_rotate.geometry('350x200')


    input_angle_lable=Label(window_rotate, font='Helvetica 12 bold', text = 'Введите угол поворота:').place(x=30, y=30)
   
    input_angle_entry=Entry(window_rotate, width=7)
    input_angle_entry.place(x=240, y=27)

    # input_angle_button=Button(window_rotate, text='←', command=lambda: input_angle(angle, input_angle_entry))
    # input_angle_button.place(x=310, y=27, height=25, width=30)

    text='Введите точку,относительно\n\
которой поворачивать кролика:'
    input_coord_lable=Label(window_rotate, font='Helvetica 12 bold', text = text, justify=LEFT).place(x=30, y=70)

    input_x_label=Label(window_rotate, font='Helvetica 12', text='X =').place(x=30, y=125)
    input_x=Entry(window_rotate, width=7)
    input_x.place(x=65, y=122)

    input_y_label=Label(window_rotate, font='Helvetica 12', text='Y =').place(x=210, y=125)
    input_y=Entry(window_rotate, width=7)
    input_y.place(x=240, y=122)

    # input_coor_button=Button(window_rotate, text='←', command=lambda:input_center(input_x, input_y))
    # input_coor_button.place(x=310, y=120, height=25, width=30)

    rotate_button=Button(window_rotate, font='Helvetica 12', text='Повернуть', command= lambda:input_rotate(input_angle_entry, input_x, input_y))
    rotate_button.place(x=220, y=155)

    input_x.insert(0,200)
    input_y.insert(0,200)
    input_angle_entry.insert(0,180)

    # print(angle)

    window_rotate.mainloop()