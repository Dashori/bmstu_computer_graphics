import ui
from tkinter import *
from tkinter import messagebox
import func
import draw

points=[]
back_points=[]
min_distance=[]
count = 0

count_back=[]
min_distance_back=[]
back_command = []

table_width = 350

## функция для считывания точки из полей ввода
def add_point_field():
    try:
        x=float(ui.add_point_entry_x.get())
        y=float(ui.add_point_entry_y.get())
    except:
        messagebox.showerror('Ошибка','Координаты точки- вещественные числа')
        return 
    
    add_point(x, y)


## функция для добавления точки в таблицу
def add_point(x, y):

    points.append([x,y])
    global count
    count += 1

    global min_distance
    min_distance.append(0)

    update_table()
    print(points)
    print(count)

    global back_command
    text = 'del_point(' + str(count) + ')'
    back_command.append(text)

    func.radius = -1
    draw.print_points()


## функция для обновления таблицы
def update_table():
    global count, table_width

    ui.tb.config(state='normal')
    ui.tb.delete(0.0, END)
    ui.mytable.clear()

    const = int(table_width/75)

    ui.mytable.field_names = [' '*const + 'Номер' + ' '*const, ' '*const + 'X' + ' '*const, ' '*const + 'Y' + ' '*const]

    for i in range(count):
        x = str(round(points[i][0], 2)) 
        y = str(round(points[i][1], 2))
        ui.mytable.add_row([str(i + 1), x, y])

    ui.tb.insert(INSERT, ui.mytable)
    ui.tb.config(state='disable')
    

## функция для проверки номера точки
def check_point(number):
    try:
        index = int(number)
    except:
        messagebox.showerror('Ошибка','Неправильно введён номер точки. Номер точки- целое число.')
        return 1

    global count

    if (count == 0):
        messagebox.showinfo('Информация','Множество точек пусто.')
        return 1

    if (index < 1 or index > count):
        messagebox.showerror('Ошибка','''Неправильно введён номер точки. Номер точки должен быть целым число и не превосходить количество точек множества.''')
        return 1

    return 0

## функция для возврата точек
def back_points_func(x, y, num):
    global points, count
   
    points.insert(num - 1, [x,y])
    count += 1

    update_table()
    draw.print_points()
    global min_distance
    min_distance.append(0)

    text = "print('!')"
    back_command.append(text)


## фукция для удаления точки
def del_point(number):
    if (check_point(number) == 1):
        return
    
    global back_command
    global points, back_points

    text = "back_points_func(" + str(points[int(number) - 1][0]) + ',' + str(points[int(number) - 1][1]) + ',' + str(int(number)) + ')'
    back_command.append(text)

    global min_distance, count
    min_distance.pop(int(number) - 1)

    points.pop(int(number) - 1)
    count -= 1

    func.radius = -1
    draw.print_points()
    update_table()


## функция для изменения координат точки
def change_point(number, x, y):
    if (check_point(number) == 1):
        return

    try:
        num_x = float(x)
        num_y = float(y)
    except:
        messagebox.showerror('Ошибка','Координаты точек- вещесвтенные числа.')
        return

    global back_command
    text = "change_point(" + str(number) +"," + str(points[int(number) - 1][0]) +',' + str(points[int(number) - 1][1]) + ')'
    back_command.append(text)

    points[int(number) - 1] = [num_x, num_y]

    func.radius = -1
    update_table()
    draw.print_points()


## обратная функция к очистке всего
def return_points(radius = 0):
    global points, back_points, count, min_distance
    points = back_points.copy()
    count = len(points)
    min_distance = [0] * count

    update_table()
    draw.print_points()
    print(radius)
    # if (radius != 0):
        # draw.print_circle_canva()
    text = "print('!')"
    back_command.append(text)


## функция для очистки всех полей и массива
def clean_all():
    global points, back_points
    back_points = points.copy()
    global back_command
    print(func.radius)
    # if (func.radius != -1):
    #     text = "return_points(" + str(func.radius) +")"
    # else:
    text = "return_points()"
    back_command.append(text)

    points.clear()

    global min_distance
    min_distance.clear()

    global count
    count = 0

    func.radius = -1

    ui.add_point_entry_x.delete(0,'end')
    ui.add_point_entry_y.delete(0,'end')

    ui.change_point_entry_x.delete(0,'end')
    ui.change_point_entry_y.delete(0,'end')

    ui.change_point_entry.delete(0,'end')
    
    ui.del_point_entry.delete(0,'end')

    ui.tb.config(state='normal')
    ui.tb.delete(0.0, END)
    ui.mytable.clear()
    ui.tb.config(state='disable')

    ui.canv.delete("all")
    draw.print_arrows()
    
    ui.solve_text.config(state='normal')
    ui.solve_text.delete(0.0, END)
    ui.solve_text.config(state='disable')


## функция для обратного действия
def back():
    global back_command, count
    global points

    if (len(back_command) == 0):
        messagebox.showinfo("Информация", "Вы выполнили все обратные действия.")
        return

    eval(back_command[len(back_command) - 1])
    back_command.pop(len(back_command) - 1)
    back_command.pop(len(back_command) - 1)
