
from tkinter import *
from tkinter.tix import MAIN
import main, draw, analysis

const_bg = "#ffffff"
const_draw = (0,0,0)

window_size_X = 800
window_size_Y = 800

window=Tk()
window.title('Lab 4 Chepigo Darya IU7-44B')
window.geometry('1400x1000')

def config(event):
    if event.widget == window:
        global window_size_X, window_size_Y

        window_size_X=window.winfo_width()/800
        window_size_Y=window.winfo_height()/800

        canv.place(x=250*window_size_X, y=40*window_size_Y-10, width=530*window_size_X, height=700*window_size_Y)

        ## условие
        task_button.place(x=400*window_size_X, y=750*window_size_Y, width=120*window_size_X, height=30*window_size_Y)

        ## о программе
        info_button.place(x=540*window_size_X, y=750*window_size_Y, width=120*window_size_X, height=30*window_size_Y)

        ## очистить канву
        clean_canvas_but.place(x=250*window_size_X, y=750*window_size_Y, width=120*window_size_X, height=30*window_size_Y)

        ## выход 
        exit_button.place(x=680*window_size_X, y=750*window_size_Y, width=100*window_size_X, height=30*window_size_Y)


        width_but = 200*window_size_X
        height_but = 30*window_size_Y
        x_but = 20*window_size_X

        ## таблица точек
        table_lab.place(x=x_but, y=50*window_size_Y, width=width_but, height=height_but)

        ## задержка    
        is_delay_check.place(x=window_size_X - 85, y=500*window_size_Y, width=width_but, height=height_but)

        ## замкнуть
        lock_but.place(x=x_but, y=550*window_size_Y, width=width_but, height=height_but)

        ## закрасить
        fill_but.place(x=x_but, y=600*window_size_Y, width=width_but, height=height_but)
        
        ## время
        time_but.place(x=x_but, y=650*window_size_Y, width=width_but, height=height_but)

        ## цвет
        color_bg.place(x=x_but, y=700*window_size_Y, width=width_but, height=height_but)
        color_draw.place(x=x_but, y=750*window_size_Y, width=width_but, height=height_but)


      
window.bind("<Configure>", config)
canv = Canvas(window, bg = "white")


##
## таблица точек
##

table_lab=Label(text='Таблица точек',font = 'Helvetica 14 bold')

##
## добавить точку
##

##
## задержка
##

is_delay = IntVar()
is_delay_check = Checkbutton(text="Задержка",font = 'Helvetica 16', variable=is_delay)

##
## замкнуть
##

lock_but=Button(text='Замкнуть',font = 'Helvetica 14 bold')

##
## закрасить
##

fill_but=Button(text='Закрасить',font = 'Helvetica 14 bold')#, command = lambda: main.change_bg())


##
## время
##

time_but=Button(text='Измерить время',font = 'Helvetica 14 bold')

##
## Выбрать цвет фона
##

color_bg=Button(text='Выбрать цвет фона',font = 'Helvetica 14 bold', command = lambda: main.change_bg())


##
## Выбрать цвет рисования
##

color_draw=Button(text='Выбрать цвет для отрисовки',font = 'Helvetica 14 bold',  command = lambda: main.change_draw())

##
## Построение фигуры
##

draw_figure_label=Label(text='Построение фигуры', font = 'Helvetica 14 bold')

##
## Очистить канвас
##

clean_canvas_but=Button(font='Helvetica 14 bold', text = 'Очистить канвас', command= lambda: canv.delete("all"))

##
## Инфо и условие
##

task_button=Button(font='Helvetica 14 bold', text = 'Условие', command= lambda: main.task_programm())

info_button=Button(font='Helvetica 14 bold', text = 'О программе', command= lambda: main.info_programm())


##
## Выход
##

exit_button=Button(font='Helvetica 14 bold', text='Выход', command= lambda: window.destroy())

window.mainloop()
