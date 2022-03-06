from tkinter import messagebox

def info_programm():
    messagebox.showinfo("Информация", "Данная программа может поворчавать, перемещать и масштабировать кролика. Чепиго Дарья ИУ7-44Б")


## функция для округления чисел
def round_numbers(num):
    if (num < 5):
        num = round(num,2)
    else:
        num = int(num)
    return num

    