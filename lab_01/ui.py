# Определить радиус и центр окружности минимального радиуса, проходящей
# хотя бы через три различные точки заданного множества точек на плоскости, притом,
# одна из точек является такой, что сумма расстояний от неѐ до остальных точек всего
# множества минимальна.

from tkinter import *
import ui_func
import func
import draw
from prettytable import PrettyTable

window=Tk()
window.title('Lab 1 Chepigo Darya IU7-44B')
window.geometry('1400x800')

def config(event):
    if event.widget == window:

        window_size_X=window.winfo_width()/1400
        window_size_Y=window.winfo_height()/800

        ## условие
        task_label.place(x=20 * window_size_X, y=30 * window_size_Y)
        task_text_label.place(x=20* window_size_X, y=60* window_size_Y)

        ## примечаниe
        notice_name_label.place(x=750 * window_size_X, y=30 * window_size_Y) 
        notice_text_label.place(x=750 * window_size_X, y=60 * window_size_Y)

        ## таблица
        tb.place(x=20 * window_size_X, y=150 * window_size_Y, width=350 * window_size_X, height = 600 * window_size_Y)
        
        ## добавить точку
        add_point_label.place(x=400 * window_size_X, y=150 * window_size_Y)

        coordinate_new_label_x.place(x=400 * window_size_X, y=174  * window_size_Y)
        coordinate_new_label_y.place(x=540 * window_size_X, y=174 * window_size_Y)

        add_point_entry_x.place(x=460 * window_size_X, y=170 * window_size_Y, width=50 * window_size_X)
        add_point_entry_y.place(x=600 * window_size_X, y=170 * window_size_Y, width=50 * window_size_X)

        add_point_button.place(x=670 * window_size_X, y=167 * window_size_Y, width=100 * window_size_X, height = 30 * window_size_Y)

        ## удалить точку
        del_point_label.place(x=400 * window_size_X, y=240 * window_size_Y)
        del_point_num_label.place(x=400 * window_size_X, y=270 * window_size_Y)
        del_point_entry.place(x=580 * window_size_X, y=270 * window_size_Y, width=50 * window_size_X)
        del_point_button.place(x=670 * window_size_X, y=267 * window_size_Y, width=100 * window_size_X, height = 30 * window_size_Y)

        ## изменеть точку
        change_point_label.place(x=400 * window_size_X, y=325 * window_size_Y)
        change_point_num_label.place(x=400 * window_size_X, y=355 * window_size_Y)
        change_point_entry.place(x=580 * window_size_X, y=355 * window_size_Y, width=50 * window_size_X)

        change_coordinate_label_x.place(x=400 * window_size_X, y=385 * window_size_Y)
        change_coordinate_label_y.place(x=540 * window_size_X, y=385 * window_size_Y)

        change_point_entry_x.place(x=460 * window_size_X, y=386 * window_size_Y, width=50 * window_size_X)
        change_point_entry_y.place(x=600 * window_size_X, y=385 * window_size_Y, width=50 * window_size_X)

        change_point_button.place(x=670 * window_size_X, y=385 * window_size_Y)


        ## Кнопочки

        clean_button.place(x=400 * window_size_X, y=450 * window_size_Y, width=300 * window_size_X, height = 30 * window_size_Y)
        solve_button.place(x=400 * window_size_X, y=500 * window_size_Y, width=180 * window_size_X, height = 30 * window_size_Y)
        back_to_canva.place(x=595 * window_size_X, y=500 * window_size_Y, width=180 * window_size_X, height = 30 * window_size_Y)

        
        back_button.place(x=400 * window_size_X, y=550 * window_size_Y)
        exit_button.place(x=595 * window_size_X, y=550 * window_size_Y)

        ## решение
        solve_name_label.place(x=400 * window_size_X, y=600 * window_size_Y)
        solve_text.place(x=405 * window_size_X, y= 630 * window_size_Y, height = 150 * window_size_Y)

        # draw.const = draw.const * window_size_X
        draw.const_x = draw.const * window_size_X
        draw.const_y = draw.const * window_size_Y

        print("draw x y", draw.const_x, draw.const_y)

        canv.place(x = 790 * window_size_X - 10, y = 180 * window_size_Y - 10, width = draw.const * 2 * window_size_X, height= draw.const * 2* window_size_Y)
        
        draw.print_points()

        print(window_size_X, window_size_Y)

        

window.bind("<Configure>", config)

##
## Условие
##

task_label=Label(font='Helvetica 12 bold', text='Условие задачи:')
task_label.place(x=20, y=30)

task_text_label=Label(font='Helvetica', justify=LEFT, text='Определить радиус и центр окружности минимального радиуса, проходящей хотя бы\n\
через три различные точки заданного множества точек на плоскости, притом, одна из точек\n\
является такой, что сумма расстояний от неѐ до остальных точек всего множества минимальна.')

##
## Примечание
##

notice_name_label=Label(font='Helvetica 12 bold', text='Примечание:')

notice_text= '1. Синим выделена точка, у которой сумма всех расстояний до неё минимальна\n\
2. Зелёным выделена новая точка- центр окружности\n\
3. На канве можно "тыкнуть" точку в диапазоне [-320,320]\n\
точки с координатами, не из этого диапазона следует вводить с клавиатуры'
notice_text_label=Label(font='Helvetica', justify=LEFT, text=notice_text)

##
## Таблица точек
##

mytable = PrettyTable()
mytable.field_names = [' Номер ', '     X     ', '     Y     ']

tb = Text(width=40, height=36, background='light grey')
tb.config(state='disable')
tb.insert(INSERT, mytable)


##
## Добавление новой точки
##

add_point_label=Label(font='Helvetica 12 bold', text='Добавить точку:')

coordinate_new_label_x=Label(font='Helvetica', text='X     =')

coordinate_new_label_y=Label(font='Helvetica', text='Y     =')

add_point_entry_x=Entry(font='Helvetica')

add_point_entry_y=Entry(font='Helvetica')

add_point_button=Button(font='Helvetica', text='Добавить', command=lambda: ui_func.add_point_field()) 

##
## Удаление точки
##

del_point_label=Label(font='Helvetica 12 bold', text='Удалить точку:')

del_point_num_label=Label(font='Helvetica', text='Введите номер точки:')

del_point_entry=Entry(font='Helvetica')

del_point_button=Button(font='Helvetica', text='Удалить', command= lambda: ui_func.del_point(del_point_entry.get()))

##
## Изменение точки
##

change_point_label=Label(font='Helvetica 12 bold', text='Изменить точку:')

change_point_num_label=Label(font='Helvetica', text='Введите номер точки:')

change_point_entry=Entry(font='Helvetica')

change_coordinate_label_x=Label(font='Helvetica', text='X     =')
change_coordinate_label_y=Label(font='Helvetica', text='Y     =')

change_point_entry_x=Entry(font='Helvetica')
change_point_entry_y=Entry(font='Helvetica')

change_point_button=Button(font='Helvetica', text='Изменить', command=lambda: ui_func.change_point(change_point_entry.get()))

##
## Очистка множества точек
##

clean_button=Button(font='Helvetica 12 bold', text = 'Очистить множество точек', command=lambda: ui_func.clean_all())

##
## Откат назад
##

back_button=Button(font='Helvetica 12 bold', text = 'Шаг назад', command= lambda:func.back())


##
## Решение
##

solve_button=Button(font='Helvetica 12 bold', text = 'Решить задачу', command= lambda: func.find_min_circle())


##
## Вывод решения текстом
##

solve_name_label=Label(font='Helvetica 12 bold', text='Результат решения задачи:')


solve_text=Text(width=40, background='light grey')
solve_text.config(state='disable')

##
## Возврат на канву
##

back_to_canva=Button(font='Helvetica 12 bold', text = 'Вернуться к канве', command= lambda: draw.print_points())


##
## Выход
##

exit_button=Button(font='Helvetica 12 bold', text='Выход', command= lambda: window.destroy())


canv = Canvas(window, bg = "white")
# canv.place(x = 750, y = 150, width = 640, height = 640)

draw.input_points_canvas()

# window.configure(bg = "white")
window.mainloop()
