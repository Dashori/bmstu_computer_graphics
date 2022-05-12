from re import I
from tkinter import *
from tkinter.tix import MAIN
import main, draw

const_bg = '#ffffff'
const_draw ='#12d9d9'
const_line = '#000002'

window_size_X = 800
window_size_Y = 800

width_but = 200

image_canvas = None

window = Tk()
window.title("Lab 7 Chepigo Darya IU7-44B")
window.geometry("1400x1000")


def config(event):
    if event.widget == window:
        global window_size_X, window_size_Y, width_but, image_canvas

        window_size_X = window.winfo_width() / 800
        window_size_Y = window.winfo_height() / 800

        ## условие
        task_button.place(x=400 * window_size_X,y=750 * window_size_Y,width=120 * window_size_X,height=30 * window_size_Y)

        ## о программе
        info_button.place(x=540 * window_size_X,y=750 * window_size_Y,width=120 * window_size_X,height=30 * window_size_Y)

        ## очистить канву
        clean_canvas_but.place(x=250 * window_size_X,y=750 * window_size_Y,width=120 * window_size_X,height=30 * window_size_Y,)

        ## выход
        exit_button.place(x=680 * window_size_X,y=750 * window_size_Y,width=100 * window_size_X,height=30 * window_size_Y,)

        width_but = 200 * window_size_X
        height_but = 30 * window_size_Y
        x_but = 20 * window_size_X

        add_point_label.place(x=x_but, y=40  * window_size_Y)

        ## добавить отрезок 1 точка
        coordinate_new_label_x1.place(x=x_but, y=84 * window_size_Y)
        coordinate_new_label_y1.place(x=130 * window_size_X, y=84 * window_size_Y)

        add_point_entry_x1.place(x=60 * window_size_X, y=80 * window_size_Y, width=50 * window_size_X)
        add_point_entry_y1.place(x=170 * window_size_X, y=80 * window_size_Y, width=50 * window_size_X)

        ## добавить отрезок 2 точка
        coordinate_new_label_x2.place(x=x_but, y=134 * window_size_Y)
        coordinate_new_label_y2.place(x=130 * window_size_X, y=134 * window_size_Y)

        add_point_entry_x2.place(x=60 * window_size_X, y=130 * window_size_Y, width=50 * window_size_X)
        add_point_entry_y2.place(x=170 * window_size_X, y=130 * window_size_Y, width=50 * window_size_X)

        add_but.place(x=x_but, y=185 * window_size_Y, width=width_but, height=30 * window_size_Y)
        draw_add_but.place(x=x_but, y=235 * window_size_Y, width=width_but, height=30 * window_size_Y)

        ## добавить отсекатель 1 точка

        add_rect_label.place(x=x_but, y=290 * window_size_Y)

        rect_coordinate_new_label_x1.place(x=x_but, y=324 * window_size_Y)
        rect_coordinate_new_label_y1.place(x=130 * window_size_X, y=324 * window_size_Y)

        add_rect_entry_x1.place(x=60 * window_size_X, y=320 * window_size_Y, width=50 * window_size_X)
        add_rect_entry_y1.place(x=170 * window_size_X, y=320 * window_size_Y, width=50 * window_size_X)

        ## добавить отсекатель 2 точка
        rect_coordinate_new_label_x2.place(x=x_but, y=374  * window_size_Y)
        rect_coordinate_new_label_y2.place(x=130 * window_size_X, y=374 * window_size_Y)

        add_rect_entry_x2.place(x=60 * window_size_X, y=370 * window_size_Y, width=50 * window_size_X)
        add_rect_entry_y2.place(x=170 * window_size_X, y=370 * window_size_Y, width=50 * window_size_X)

        add_rect.place(x=x_but, y=425 * window_size_Y, width=width_but, height=30 * window_size_Y)
        draw_rect_but.place(x=x_but, y=475 * window_size_Y, width=width_but, height=30 * window_size_Y)

        ## отсечь
        cutoff_but.place(x=x_but, y=520 * window_size_Y, width=width_but, height=height_but)

        empty.place(x=x_but, y=560 * window_size_Y)
        canv.place(x=250 * window_size_X,y=40 * window_size_Y, width=530 * window_size_X,height=700 * window_size_Y)

window.bind("<Configure>", config)
canv = Canvas(window, bg="white")

##
## лишнее место
##

text_empty = '''
Здесь можно добавить ещё
какие-то функции, например, 
менять цвет фона и объектов
но я хотела спать и уже 
не стала это фиксить.'''


empty=Label(font='Helvetica 20', text=text_empty, justify=LEFT)

##
## добавить отрезок
##

add_point_label=Label(font='Helvetica 14 bold', text='Введите координаты отрезка:')

coordinate_new_label_x1=Label(font='Helvetica', text='X_1     =')
coordinate_new_label_y1=Label(font='Helvetica', text='Y_1     =')

add_point_entry_x1=Entry(font='Helvetica')
add_point_entry_y1=Entry(font='Helvetica')


coordinate_new_label_x2=Label(font='Helvetica', text='X_2     =')
coordinate_new_label_y2=Label(font='Helvetica', text='Y_2     =')

add_point_entry_x2=Entry(font='Helvetica')
add_point_entry_y2=Entry(font='Helvetica')

add_but = Button(text="Добавить отрезок", font="Helvetica 13 bold",
command= lambda: draw.input_line(add_point_entry_x1, add_point_entry_y1, add_point_entry_x2, add_point_entry_y2 ))
draw_add_but = Button(text="Нарисовать отрезок", font="Helvetica 13 bold", command= lambda: draw.input_points_canvas())


##
## добавить отсекатель
##

add_rect_label=Label(font='Helvetica 14 bold', text='Введите координаты отсекателя:')

rect_coordinate_new_label_x1=Label(font='Helvetica', text='X_1     =')
rect_coordinate_new_label_y1=Label(font='Helvetica', text='Y_1     =')

add_rect_entry_x1=Entry(font='Helvetica')
add_rect_entry_y1=Entry(font='Helvetica')


rect_coordinate_new_label_x2=Label(font='Helvetica', text='X_2     =')
rect_coordinate_new_label_y2=Label(font='Helvetica', text='Y_2     =')

add_rect_entry_x2=Entry(font='Helvetica')
add_rect_entry_y2=Entry(font='Helvetica')


add_rect = Button(text='Добавить отсекатель', font="Helvetica 13 bold", 
command= lambda: draw.input_rect(add_rect_entry_x1, add_rect_entry_y1, add_rect_entry_x2, add_rect_entry_y2))
draw_rect_but = Button(text="Нарисовать отсекатель", font="Helvetica 13 bold", command= lambda: draw.input_rect_canvas())


##
## отсечь 
##

cutoff_but = Button(text='Отсечь', font="Helvetica 13 bold", command= lambda: draw.cutoff())

##
## Очистить канвас
##

clean_canvas_but = Button(font="Helvetica 14 bold", text="Очистить канвас", command=lambda: draw.clean())

##
## Инфо и условие
##

task_button = Button(font="Helvetica 14 bold", text="Условие", command=lambda: main.task_programm())

info_button = Button(font="Helvetica 14 bold", text="О программе", command=lambda: main.info_programm())


##
## Выход
##

exit_button = Button(font="Helvetica 14 bold", text="Выход", command=lambda: window.destroy())


window.mainloop()
