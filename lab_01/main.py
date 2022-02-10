import ui
from tkinter import *
from tkinter import  messagebox

points=[]
count = 0

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
        global count
        count += count_input
        

def read_points(count_input):
    count_input = int(count_input)
    try:
        for i in range(count_input):
            float(ui.name_entry_x[i].get())
            float(ui.name_entry_y[i].get())  
    except:
        text='Координаты точек- вещесвтенные числа. Количество точек должно соответствовать ' + str(count) + '.'
        messagebox.showerror('Ошибка',text)
        return
    for i in range(count_input):
        points.append([float(ui.name_entry_x[i].get()), float(ui.name_entry_y[i].get())]) 
        ui.name_entry_x[i].config(state='readonly')
        ui.name_entry_y[i].config(state='readonly')

    ui.input_table_button.config(state='disable')

    print(points)


def clean_all(count_input):
    points.clear()
    global count
    count = 0

    for i in range(int(count_input)):
        ui.name_entry_x[i].config(state='normal')
        ui.name_entry_x[i].delete(0, 'end')
        ui.name_entry_x[i].config(state='readonly')

        ui.name_entry_y[i].config(state='normal')
        ui.name_entry_y[i].delete(0, 'end')
        ui.name_entry_y[i].config(state='readonly')

    ui.input_count.config(state='normal')
    ui.input_count.delete(0,'end')
    
    print(points)

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

def print_table():

    window=Tk()
    window.title('Table')
    window.geometry('300x600')  

    
    window.resizable(width=False, height=False)
    window.mainloop()

    
        