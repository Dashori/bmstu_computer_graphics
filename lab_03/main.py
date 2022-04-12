from tkinter import *
from tkinter import messagebox, colorchooser
import ui

def task_programm():
    messagebox.showinfo("Информация",
'''Данная программа реализует и исследует
алгоритмы построения отрезков.

Алгоритмы: 
-ЦДА
-Брезенхем действительные числа
-Брезенхем целые числа
-Брезенхем с устранением ступенчатости
-ВУ''')

def info_programm():
    messagebox.showinfo("Информация","Лабораторна работа №3. Чепиго Дарья ИУ7-44Б")


## функция для считывания координат х и у из полей ввода
def input_coor(input_x, input_y):
    x=input_x.get()
    y=input_y.get()

    try:
        x=float(input_x.get())
        y=float(input_y.get())
        return x,y
    except:
        messagebox.showerror("Ошибка","Неправильно ввёдены числовые значения.")
        input_x.delete(0,'end')
        input_y.delete(0,'end')
        return 


## функция для закрытие окошка и возврата кнопки в состояние нормал
def exit_window(root, button):
    root.destroy()


def change_window_canv():
    ui.canv.config(bg=ui.const_bg[1])


def change_bg():
    ui.const_bg = colorchooser.askcolor()
    change_window_canv()


def change_draw():
    a = colorchooser.askcolor()
    ui.const_draw = a[0]
    