from re import I
from tkinter import *
from tkinter.tix import MAIN
import main, draw
from prettytable import PrettyTable

const_bg = '#ffffff'
const_draw ='#12d9d9'
const_line = '#000002'

window_size_X = 800
window_size_Y = 800

width_but = 200

image_canvas = None

window = Tk()
window.title("Lab 6 Chepigo Darya IU7-44B")
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

        ## таблица точек
        table_lab.place(x=x_but, y=40 * window_size_Y, width=width_but, height=height_but)

        tb.place(x=20 * window_size_X,y=70 * window_size_Y,width=width_but,height=380 * window_size_Y)

        ## добавить
        add_but.place(x=x_but,y=470 * window_size_Y,width=width_but, height=30 * window_size_Y)

        seed_pixel.place(x=x_but, y=510 * window_size_Y, width=width_but / 2, height=30 * window_size_Y)
        seed_pixel_input.place(x=x_but + width_but / 2, y=510 * window_size_Y, width=width_but / 2, height=30 * window_size_Y)

        ## задержка
        is_delay_check.place(x=x_but - 15,y=550 * window_size_Y,width=80 * window_size_X,height=height_but)

        ## замкнуть
        lock_but.place(x=x_but, y=590 * window_size_Y, width=width_but, height=height_but)

        ## закрасить
        fill_but.place(x=x_but, y=640 * window_size_Y, width=width_but, height=height_but)

        ## цвет
        color_bg.place(x=x_but, y=690 * window_size_Y, width=width_but, height=height_but)
        color_draw.place(x=x_but, y=750 * window_size_Y, width=width_but, height=height_but)

        canv.place(x=250 * window_size_X,y=40 * window_size_Y, width=530 * window_size_X,height=700 * window_size_Y)

        image_canvas = PhotoImage(width = window.winfo_width(), height = window.winfo_height())
        canv.create_image((window.winfo_width() / 2, window.winfo_height() / 2), image = image_canvas, state = "normal")




window.bind("<Configure>", config)
canv = Canvas(window, bg="white")


##
## таблица точек
##

table_lab = Label(text="Таблица точек", font="Helvetica 14 bold")
mytable = PrettyTable()
tb = Text(background="light grey")
tb.config(state="disable")
tb.insert(INSERT, mytable)

##
## добавить точку
##

add_but = Button(text="Добавить точку", font="Helvetica 13 bold", command= lambda: draw.add_point_window())

##
## ткнуть затравку
##

seed_pixel = Button(text='Отметить затравку', font="Helvetica 13 bold", command= lambda: draw.touch_pixel_window())

##
## ввести затравку
##

seed_pixel_input = Button(text='Ввести затравку', font="Helvetica 13 bold", command= lambda: draw.add_pixel_window())


##
## задержка
##

is_delay = IntVar()
is_delay.set(0)
is_delay_check = Checkbutton(text="Задержка", font="Helvetica 16", variable=is_delay)

##
## замкнуть
##

lock_but = Button(text="Замкнуть", font="Helvetica 14 bold", command= lambda: draw.lock_edge())

##
## закрасить
##

fill_but = Button(text="Закрасить", font="Helvetica 14 bold", command = lambda: draw.fill_figure())

##
## Выбрать цвет фонa
##

color_bg = Button(text="Выбрать цвет фона", font="Helvetica 14 bold", command=lambda: main.change_bg())


##
## Выбрать цвет заполнения
##

color_draw = Button(text="Выбрать цвет для заполнения",font="Helvetica 14 bold",command=lambda: main.change_draw())

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




draw.input_points_canvas()
window.mainloop()
