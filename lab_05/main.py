from tkinter import *
from tkinter import messagebox, colorchooser
import ui, draw


points=[]

def task_programm():
    messagebox.showinfo(
        "Условие",
        """Данная программа реализует и исследует
алгоритмы растрового заполнения сплошных областей.
Алгоритм заполнения: по ребрам.
""")


def info_programm():
    messagebox.showinfo("Информация", "Лабораторна работа №5. Чепиго Дарья ИУ7-44Б")


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
