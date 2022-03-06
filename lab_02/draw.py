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

inside_rabbit= [[2, 4], [6, 8], [4, 30], [5, 31], [6, 31], [8, 31], [9, 31],
[9, 30], [1, 30], [32, 9], [32, 10], [32, 12], [32, 29], [35, 12], [10, 12],
[29,12], [29, 15], [29, 17], [29, 23], [23, 17], [22, 33], [33, 17], [20, 33],
[34, 24], [34, 25], [34, 26], [34, 27], [34, 28], [24, 28]] ##хвост

center_x=200
center_y=270

const = 325
const_x = 325
const_y = 325

const_cutoff = 60
index_cutoff_x = 5
index_cutoff_y = 5

text_y = 325
text_x = 325


def print_rabbit(x = center_x, y = center_y):
    global contour_rabbit
    ui.canv.delete("all")
    print_arrows()

    for i in range(28):
        x1 = contour_rabbit[i][0] + center_x 
        y1 = contour_rabbit[i][1] + center_y

        x2 = contour_rabbit[i+1][0] + center_x
        y2 = contour_rabbit[i+1][1] + center_y
        ui.canv.create_line(x1, y1, x2, y2, width=4)

    ui.canv.create_line(contour_rabbit[0][0] + center_x, contour_rabbit[0][1] + center_y,
    contour_rabbit[28][0] + center_x, contour_rabbit[28][1] + center_y, width=4)

    for i in range(len(inside_rabbit) - 1):
        x1 = contour_rabbit[inside_rabbit[i][0] - 1][0] + center_x
        y1 = contour_rabbit[inside_rabbit[i][0] - 1][1] + center_y

        x2 = contour_rabbit[inside_rabbit[i][1] - 1][0] + center_x
        y2 = contour_rabbit[inside_rabbit[i][1] - 1][1] + center_y

        ui.canv.create_line(x1, y1, x2, y2, width=2)

    print("x, y", x, y)

    ui.canv.create_oval(x + center_x, y + center_y, x + center_x + 4, y + center_y + 4, fill='grey')


def input_rotate(input_angle_entry, input_x, input_y):
    angle=input_angle(input_angle_entry)
    center=input_center(input_x, input_y)

    if (angle == None or center == None):
        return

    x,y = center[0]+ const_x - center_x, center[1] + const_y - center_y
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
    rotate_button.place(x=220, y=155)

    input_x.insert(0,0)
    input_y.insert(0,0)
    input_angle_entry.insert(0,10)

    window_rotate.mainloop()


## функция для прорисовки осей
def print_arrows():
    ui.canv.create_line(const_x, const_y*2, const_x, 0, width=2, arrow=LAST, fill='grey') 
    ui.canv.create_line(0, const_y, const_x*2, const_y, width=2, arrow=LAST, fill='grey')

    ## x
    for line in range(int(const_x), int(const_x) * 2, const_cutoff):
        ui.canv.create_line([(line, int(const_y) - 4), (line, int(const_y) + 4)], width = 3, fill='grey')
    for line in range(int(const_x), 0, -const_cutoff):
        ui.canv.create_line([(line, int(const_y) - 4), (line, int(const_y) + 4)], width = 3, fill='grey')
    ## y
    for line in range(int(const_y), int(const_y) * 2, const_cutoff):
        ui.canv.create_line([(int(const_x) - 4, line), (int(const_x) + 4,line)], width = 3, fill='grey')
    for line in range(int(const_y), 0, -const_cutoff):
        ui.canv.create_line([(int(const_x) - 4, line), (int(const_x) + 4,line)], width = 3, fill='grey')

    global text_x

    ## текст x
    text_points_x = []
    for i in range(1, index_cutoff_x + 2):
        x = text_x * i/(index_cutoff_x)
        text_points_x.append(func.round_numbers(x))
        
    ## текст y
    text_points_y = []
    for i in range(1,index_cutoff_y + 2):
        y = text_y * i/(index_cutoff_y)
        text_points_y.append(func.round_numbers(y))
    point_text = -2

    ## x +
    for line in range(int(const_x), int(const_x) * 2, const_cutoff):
        point_text += 1
        if (point_text == -1):
            ui.canv.create_text(line + 10, const_y - 10, 
            text=str(0), justify=LEFT, font=('Helvetica 10'), fill='grey')
            continue

        ui.canv.create_text(line - 10, const_y - 10, 
        text=str(text_points_x[point_text]), justify=LEFT, font=('Helvetica 10'), fill='grey')
        
    ## x-
    point_text = -2
    for line in range(int(const_x), 0, -const_cutoff):
        point_text += 1
        if (point_text == -1):
            continue

        ui.canv.create_text(line + 10, const_y - 10, 
        text=str((-1) * text_points_x[point_text]), justify=LEFT, font=('Helvetica 10'), fill='grey')


    ## y+
    point_text = -2
    for line in range(int(const_y), int(const_y) * 2, const_cutoff):
        point_text += 1
        if (point_text == -1):
            continue

        ui.canv.create_text(const_x - 20, line, 
        text=str((-1) * text_points_y[point_text]), justify=LEFT, font=('Helvetica 10'), fill='grey')

    ## y-
    point_text = -2
    for line in range(int(const_y), 0, -const_cutoff):
        point_text += 1
        if (point_text == -1):
            continue

        ui.canv.create_text(const_x - 20, line, 
        text=str(text_points_y[point_text]), justify=LEFT, font=('Helvetica 10'), fill='grey')
