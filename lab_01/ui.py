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
window.title('Lab 1')
window.geometry('1400x800')

##
## Условие
##

task_label=Label(font='Helvetica 12 bold', text='Условие задачи:')
task_label.place(x=20, y=15)

task_text_label=Label(font='Helvetica', justify=LEFT, text='Определить радиус и центр окружности минимального радиуса, проходящей хотя бы\n\
через три различные точки заданного множества точек на плоскости, притом, одна из точек\n\
является такой, что сумма расстояний от неѐ до остальных точек всего множества минимальна.')
task_text_label.place(x=20,y=45)

##
## Таблица точек
##

mytable = PrettyTable()
mytable.field_names = [' Номер ', '     X     ', '     Y     ']

tb = Text(width=40, height=36, background='light grey')
# scroll_bar = Scrollbar(window, command = tb.yview)
# scroll_bar.pack(side = RIGHT, fill = Y)
# tb.config(yscrollcommand=scroll_bar.set)
tb.config(state='disable')
tb.place(x=20,y=150)
# tb.pack(side=tkinter.RIGHT)
tb.insert(INSERT, mytable)


##
## Добавление новой точки
##

add_point_label=Label(font='Helvetica 12 bold', text='Добавить точку:')
add_point_label.place(x=400, y=150)

coordinate_new_label=Label(font='Helvetica', text='X  =                    Y  =')
coordinate_new_label.place(x=400, y=180)

add_point_entry_x=Entry(font='Helvetica')
add_point_entry_x.place(x=440, y=177, width=50)

add_point_entry_y=Entry(font='Helvetica')
add_point_entry_y.place(x=550, y=177, width=50)

add_point_button=Button(font='Helvetica', text='Добавить', command=lambda: ui_func.add_point())
add_point_button.place(x=640, y=177, width=80, height=27)

##
## Удаление точки
##

del_point_label=Label(font='Helvetica 12 bold', text='Удалить точку:')
del_point_label.place(x=400, y=240)

del_point_num_label=Label(font='Helvetica', text='Введите номер точки:')
del_point_num_label.place(x=400, y=270)

del_point_entry=Entry(font='Helvetica')
del_point_entry.place(x=570, y=267, width=50)

del_point_button=Button(font='Helvetica', text='Удалить', command= lambda: ui_func.del_point(del_point_entry.get()))
del_point_button.place(x=640, y=267, width=80, height=27)

##
## Изменение точки
##

change_point_label=Label(font='Helvetica 12 bold', text='Изменить точку:')
change_point_label.place(x=400, y=325)

change_point_num_label=Label(font='Helvetica', text='Введите номер точки:')
change_point_num_label.place(x=400, y=355)

change_point_entry=Entry(font='Helvetica')
change_point_entry.place(x=570, y=352, width=50)

change_coordinate_label=Label(font='Helvetica', text='X  =                    Y  =')
change_coordinate_label.place(x=400, y=388)

change_point_entry_x=Entry(font='Helvetica')
change_point_entry_x.place(x=440, y=385, width=50)

change_point_entry_y=Entry(font='Helvetica')
change_point_entry_y.place(x=550, y=385, width=50)

change_point_button=Button(font='Helvetica', text='Изменить', command=lambda: ui_func.change_point(change_point_entry.get()))
change_point_button.place(x=640, y=385, width=85, height=27)

##
## Очистка множества точек
##

clean_button=Button(font='Helvetica 12 bold', text = 'Очистить множество точек', command=lambda: ui_func.clean_all())
clean_button.place(x=400, y=450)

##
## Решение
##

solve_button=Button(font='Helvetica 12 bold', text = 'Решить задачу', command= lambda: func.find_min_circle()) #func.find_min_distance(), 
solve_button.place(x=400, y=500)

##
## Выход
##

exit_button=Button(font='Helvetica 12 bold', text='Выход', command= lambda: window.destroy())
exit_button.place(x=560, y=500)


canv = Canvas(window, bg = "white")
canv.place(x = 750, y = 150, width = 640, height = 640)

draw.input_points_canvas()

window.resizable(width=False, height=False)
window.mainloop()
