# Определить радиус и центр окружности минимального радиуса, проходящей
# хотя бы через три различные точки заданного множества точек на плоскости, притом,
# одна из точек является такой, что сумма расстояний от неѐ до остальных точек всего
# множества минимальна.

from tkinter import *
from turtle import left
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
        window_size_Y=window.winfo_height()

        ## условие
        task_label.place(x=20* window_size_X, y=30,  width=event.width/6, height=event.height/19)
        task_text_label.place(x=10* window_size_X, y=60, width=event.width/1.8, height=event.height/16)

        ## примечание
        notice_name_label.place(x=760* window_size_X, y=30, width=event.width - 1290, height=event.height - 750)
        notice_text_label.place(x=760* window_size_X, y=60, width=event.width/1.8, height=event.height/12)


        ## таблица

        tb.place(x=20,y=150, width=event.width/4.4, height=event.height - 200)
        
        ## добавить точку
        add_point_label.place(x=455* window_size_X, y=130, width=event.width/10, height=event.height/25)

        coordinate_new_label_x.place(x=455 * window_size_X, y=174, width=event.width/37, height=event.height/25)
        coordinate_new_label_y.place(x=585 * window_size_X, y=174, width=event.width/37, height=event.height/25)

        add_point_entry_x.place(x=520, y=177, width=event.width/29, height=event.height/36)
        add_point_entry_y.place(x=650, y=177, width=event.width/29, height=event.height/36)

        add_point_button.place(x=740, y=174, width=event.width/18, height=event.height/30)

        ## удалить точку
        del_point_label.place(x=455, y=240, width=event.width/11, height=event.height/25)
        del_point_num_label.place(x=455, y=270, width=event.width/12, height=event.height/25)
        del_point_entry.place(x=650, y=272, width=event.width/29, height=event.height/36)
        del_point_button.place(x=740, y=267,width=event.width/18, height=event.height/30)

        ## изменеть точку
        change_point_label.place(x=455, y=325, width=event.width/10, height=event.height/25)
        change_point_num_label.place(x=455, y=355, width=event.width/12, height=event.height/25)
        change_point_entry.place(x=650, y=355, width=event.width/29, height=event.height/36)

        change_coordinate_label_x.place(x=455, y=385, width=event.width/37, height=event.height/25)
        change_coordinate_label_y.place(x=585, y=385, width=event.width/37, height=event.height/25)

        change_point_entry_x.place(x=520, y=386, width=event.width/29, height=event.height/36)
        change_point_entry_y.place(x=650, y=385, width=event.width/29, height=event.height/36)

        change_point_button.place(x=740, y=385, width=event.width/18, height=event.height/30)


        ## Кнопочки

        clean_button.place(x=455, y=450, width=event.width/6, height=event.height/30)
        solve_button.place(x=455, y=500, width=event.width/10, height=event.height/30)
        back_to_canva.place(x=650, y=500, width=event.width/8, height=event.height/30)

        
        back_button.place(x=455, y=550, width=event.width/10, height=event.height/30)
        exit_button.place(x=650, y=550, width=event.width/8, height=event.height/30)

        ## решение
        solve_name_label.place(x=455, y=600, width=event.width/6, height=event.height/30)
        solve_text.place(x=450, y=630, width=event.width/5, height=event.height/6)

        canv.place(x = 1000, y = 150, width = event.width/2, height = event.height/2)

        

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
# task_text_label.place(x=20, y=60)

##
## Примечание
##

notice_name_label=Label(font='Helvetica 12 bold', text='Примечание:')
# notice_name_label.place(x=760, y=30)

notice_text= '1. Синим выделена точка, у которой сумма всех расстояний до неё минимальна\n\
2. Зелёным выделена новая точка- центр окружности\n\
3. На канве можно "тыкнуть" точку в диапазоне [-320,320]\n\
точки с координатами, не из этого диапазона следует вводить с клавиатуры'
notice_text_label=Label(font='Helvetica', justify=LEFT, text=notice_text)
# notice_text_label.place(x=760, y=60)

##
## Таблица точек
##

mytable = PrettyTable()
mytable.field_names = [' Номер ', '     X     ', '     Y     ']

tb = Text(width=40, height=36, background='light grey')
tb.config(state='disable')
# tb.place(x=20,y=150)
tb.insert(INSERT, mytable)


##
## Добавление новой точки
##

add_point_label=Label(font='Helvetica 12 bold', text='Добавить точку:')
add_point_label.place(x=400, y=150)

coordinate_new_label_x=Label(font='Helvetica', text='X     =')
# coordinate_new_label_x.place(x=450, y=180)


coordinate_new_label_y=Label(font='Helvetica', text='Y     =')
# coordinate_new_label_y.place(x=590, y=180)


add_point_entry_x=Entry(font='Helvetica')
# add_point_entry_x.place(x=440, y=177, width=50)

add_point_entry_y=Entry(font='Helvetica')
# add_point_entry_y.place(x=550, y=177, width=50)

add_point_button=Button(font='Helvetica', text='Добавить', command=lambda: ui_func.add_point_field()) #.pack(padx=560, pady=50, expand=90)
# add_point_button.place(x=640, y=177, width=80, height=27)

# add_point_button_2 = Button(text="Button").pack(padx=10, pady=10, expand=1)

##
## Удаление точки
##

del_point_label=Label(font='Helvetica 12 bold', text='Удалить точку:')
# del_point_label.place(x=400, y=240)

del_point_num_label=Label(font='Helvetica', text='Введите номер:')
# del_point_num_label.place(x=400, y=270)

del_point_entry=Entry(font='Helvetica')
# del_point_entry.place(x=570, y=267, width=50)

del_point_button=Button(font='Helvetica', text='Удалить', command= lambda: ui_func.del_point(del_point_entry.get()))
# del_point_button.place(x=640, y=267, width=80, height=27)

##
## Изменение точки
##

change_point_label=Label(font='Helvetica 12 bold', text='Изменить точку:')
# change_point_label.place(x=400, y=325)

change_point_num_label=Label(font='Helvetica', text='Введите номер:')
# change_point_num_label.place(x=400, y=355)

change_point_entry=Entry(font='Helvetica')
# change_point_entry.place(x=570, y=352, width=50)

change_coordinate_label_x=Label(font='Helvetica', text='X     =')
# change_coordinate_label.place(x=400, y=388)
change_coordinate_label_y=Label(font='Helvetica', text='Y     =')

change_point_entry_x=Entry(font='Helvetica')
# change_point_entry_x.place(x=440, y=385, width=50)

change_point_entry_y=Entry(font='Helvetica')
# change_point_entry_y.place(x=550, y=385, width=50)

change_point_button=Button(font='Helvetica', text='Изменить', command=lambda: ui_func.change_point(change_point_entry.get()))
# change_point_button.place(x=640, y=385, width=85, height=27)

##
## Очистка множества точек
##

clean_button=Button(font='Helvetica 12 bold', text = 'Очистить множество точек', command=lambda: ui_func.clean_all())
# clean_button.place(x=400, y=450)

##
## Откат назад
##

back_button=Button(font='Helvetica 12 bold', text = 'Шаг назад', command= lambda:func.back())
# back_button.place(x=400, y=550)

##
## Решение
##

solve_button=Button(font='Helvetica 12 bold', text = 'Решить задачу', command= lambda: func.find_min_circle())
# solve_button.place(x=400, y=500)

##
## Вывод решения текстом
##

solve_name_label=Label(font='Helvetica 12 bold', text='Результат решения задачи:')
# solve_name_label.place(x=400, y=600)

solve_text=Text(width=40, background='light grey')
# solve_text.place(x=400, y=630, height=150)
solve_text.config(state='disable')

##
## Возврат на канву
##

back_to_canva=Button(font='Helvetica 12 bold', text = 'Вернуться к канве', command= lambda: draw.print_points())
# back_to_canva.place(x=560, y=500)


##
## Выход
##

exit_button=Button(font='Helvetica 12 bold', text='Выход', command= lambda: window.destroy())
# exit_button.place(x=560, y=550)


canv = Canvas(window, bg = "white")
canv.place(x = 750, y = 150, width = 640, height = 640)

draw.input_points_canvas()

# window.resizable(width=auto, height=auto)
# window.configure(bg = "white")
window.mainloop()
