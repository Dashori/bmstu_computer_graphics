from tkinter import messagebox
import ui
from tkinter import *
from tkinter import messagebox
import func
from prettytable import PrettyTable

points=[]
min_distance=[]
count = 0

## функция для проверки количества точек и изменения статуса полей для ввода
def check_count(count_input):     
    try:
        count_input = int(count_input)
    except:
        messagebox.showerror('Ошибка','Количество точек- целое число')
        ui.input_count.delete(0, 'end')
        return

    if (count_input < 0):
        messagebox.showerror('Ошибка','Количество точек- целое число')
        ui.input_count.delete(0, 'end')    
    else:
        if (count_input > 10):
            messagebox.showinfo('Информация','Введите в таблицу первые 10 точек. Остальные добавляйте по одной.')
            count_input = 10
            ui.input_count.delete(0,'end')
            ui.input_count.insert(0, 10)
        ui.input_count.config(state='readonly')

        for i in range(count_input):
            ui.name_entry_x[i].config(state='normal')
            ui.name_entry_y[i].config(state='normal')

        ui.input_table_button.config(state='normal')
        ui.count_points_button.config(state='disable')

## функция для считывания точек из таблицы
def read_points(count_input):
    count_input = int(count_input)
    try:
        for i in range(count_input):
            float(ui.name_entry_x[i].get())
            float(ui.name_entry_y[i].get())  
    except:
        text='Координаты точек- вещесвтенные числа. Количество точек должно соответствовать ' + str(count_input) + '.'
        messagebox.showerror('Ошибка',text)
        return
    for i in range(count_input):
        points.append([float(ui.name_entry_x[i].get()), float(ui.name_entry_y[i].get())]) 
        ui.name_entry_x[i].config(state='readonly')
        ui.name_entry_y[i].config(state='readonly')

    ui.input_table_button.config(state='disable')
    global count
    count += count_input

    print(points)
    
## функция для добавления точки
def add_point():
    try:
        x=float(ui.add_point_entry_x.get())
        y=float(ui.add_point_entry_y.get())
    except:
        messagebox.showerror('Ошибка','Координаты точки- вещественные числа')
        return 

    points.append([x,y])
    global count
    count += 1

    print(points)
    print(count)


## функция для печати таблицы
def print_table():

    table=Tk()
    table.title('Table')
    table.geometry('400x600')  

    scroll_bar = Scrollbar(table)
    scroll_bar.pack(side = RIGHT, fill = Y)

    mytable = PrettyTable()
    mytable.field_names = [' Номер ', '       X       ', '       Y       ']

    for i in range(count):
        x = str(points[i][0]) 
        y = str(points[i][1])
        mytable.add_row([str(i+1), x, y])
    
    tb = Text(table, width=300, height=600, background='light grey')
    tb.insert(INSERT,mytable)
    tb.pack()
    table.mainloop()


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
        messagebox.showerror('Ошибка','Неправильно введён номер точки.\
        Номер точки должен быть целым число и не превосходить количество точек множества.')
        return 1

    return 0


## фукция для удаления точки
def del_point(number):
    if (check_point(number) == 1):
        return
    
    points.pop(int(number) - 1)
    global count
    count -= 1


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


## функция для очистки всех полей и массива
def clean_all():
    points.clear()
    global count
    count = 0

    for i in range(10):
        ui.name_entry_x[i].config(state='normal')
        ui.name_entry_x[i].delete(0, 'end')
        ui.name_entry_x[i].config(state='readonly')

        ui.name_entry_y[i].config(state='normal')
        ui.name_entry_y[i].delete(0, 'end')
        ui.name_entry_y[i].config(state='readonly')

    ui.input_table_button.config(state='disable')

    ui.input_count.config(state='normal')
    ui.input_count.delete(0,'end')

    ui.count_points_button.config(state='normal')
    
    ui.add_point_entry_x.delete(0,'end')
    ui.add_point_entry_y.delete(0,'end')

    ui.change_point_entry_x.delete(0,'end')
    ui.change_point_entry_y.delete(0,'end')
    ui.change_point_entry.delete(0,'end')
    
    ui.del_point_entry.delete(0,'end')
    