# Определить радиус и центр окружности минимального радиуса, проходящей
# хотя бы через три различные точки заданного множества точек на плоскости, притом,
# одна из точек является такой, что сумма расстояний от неѐ до остальных точек всего
# множества минимальна.

from tkinter import *
import ui_func

window=Tk()
window.title('Lab 1')
window.geometry('800x600')

##
## Условие
##

task_label=Label(font='Helvetica 12 bold', text='Условие задачи:')
task_label.place(x=50, y=15)

task_text_label=Label(font='Helvetica', justify=LEFT, text='Определить радиус и центр окружности минимального радиуса, проходящей хотя бы\n\
через три различные точки заданного множества точек на плоскости, притом, одна из точек\n\
является такой, что сумма расстояний от неѐ до остальных точек всего множества минимальна.')
task_text_label.place(x=50,y=37)

##
## Количество точек множества
##

count_points_label=Label(font='Helvetica 12 bold', text='Введите количество точек множества: ')
count_points_label.place(x=50, y=110)

input_count=Entry(font='Helvetica')
input_count.place(x=370, y=107, width=50)

count_points_button=Button(text='Ввод',font='Helvetica', command = lambda: ui_func.check_count(input_count.get()))
count_points_button.place(x=430, y=107, width=55, height=25)


##
## Таблица из 10 точек
##

table_points_label=Label(font='Helvetica 12 bold', text='Таблица точек:')
table_points_label.place(x=50, y=150)

coordinate_table_label=Label(font='Helvetica', text='X                  Y')
coordinate_table_label.place(x=85, y=170)

for i in range(10):
    name_label='point_label_'+str(i + 1)
    name_label=Label(font='Helvetica', justify=LEFT, text=str(i + 1))
    name_label.place(x=50, y=200+i*30)

## массивы для полей первых 10 точек таблицы
name_entry_x = [] 
name_entry_y = []

for i in range(10):
    name_entry_x.append(Entry(font='Helvetica'))
    name_entry_x[i].place(x=72, y=198+i*30, width=50)
    name_entry_x[i].config(state='readonly')

    name_entry_y.append(Entry(font='Helvetica'))
    name_entry_y[i].place(x=150, y=198+i*30, width=50)
    name_entry_y[i].config(state='readonly')
   
input_table_button=Button(font='Helvetica', text='Добавить', command=lambda: ui_func.read_points(input_count.get()))
input_table_button.place(x=220, y=468, width=80, height=27) 
input_table_button.config(state='disable')

##
## Вывод таблицы точек
##

view_table_button=Button(font='Helvetica 12 bold', text='Вывести таблицу', command = lambda: ui_func.print_table())
view_table_button.place(x=50, y=520)

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

solve_button=Button(font='Helvetica 12 bold', text = 'Решить задачу')
solve_button.place(x=400, y=500)

##
## Выход
##

exit_button=Button(font='Helvetica 12 bold', text='Выход', command= lambda: window.destroy())
exit_button.place(x=560, y=500)

window.resizable(width=False, height=False)
window.mainloop()