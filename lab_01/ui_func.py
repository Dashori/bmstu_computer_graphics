import ui
from tkinter import *
from tkinter import messagebox
import func
import draw

points=[]
min_distance=[]
count = 0

points_back=[]
count_back=[]
min_distance_back=[]

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

    if (abs(x) > 320 or abs(y) > 320):
        func.scale_axis()

    func.radius = -1
    draw.print_points()

    


## функция для обновления таблицы
def update_table():
    global count
    ui.tb.config(state='normal')
    ui.tb.delete(0.0, END)
    ui.mytable.clear()
    ui.mytable.field_names = [' Номер ', '     X     ', '     Y     ']

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


## фукция для удаления точки
def del_point(number):
    if (check_point(number) == 1):
        return
    
    global min_distance
    min_distance.pop(int(number) - 1)

    global points
    points.pop(int(number) - 1)

    global count
    count -= 1

    print("Точки после удаления", points)
    print("Расстояния после удаления", min_distance)
    func.radius = -1
    draw.print_points()
    update_table()


## функция для изменения координат точки
def change_point(number):
    if (check_point(number) == 1):
        return
    
    x = ui.change_point_entry_x.get()
    y = ui.change_point_entry_y.get()

    try:
        num_x = float(x)
        num_y = float(y)
    except:
        messagebox.showerror('Ошибка','Координаты точек- вещесвтенные числа.')
        return

    points[int(number) - 1] = [num_x, num_y]

    func.radius = -1
    update_table()
    draw.print_points()


## функция для очистки всех полей и массива
def clean_all():
    global points
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
