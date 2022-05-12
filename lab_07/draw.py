from tkinter import *
from tkinter import messagebox

import ui

lines = []

rect = None
old_coor_rect = None

old_coor = None

INVISIBLE = 0
VISIBLE = 1

## функция для считывания координат х и у из полей ввода
def input_coor(input_x, input_y):
    x = input_x.get()
    y = input_y.get()

    try:
        x = float(input_x.get())
        y = float(input_y.get())
        return x, y
    except:
        messagebox.showerror("Ошибка", "Неправильно ввёдены числовые значения.")
        input_x.delete(0, "end")
        input_y.delete(0, "end")
        return 'a', 'b'


##функция для считывания отрезка
def input_line(input_x1, input_y1, input_x2, input_y2):
    x1, y1 = input_coor(input_x1, input_y1)

    if (x1 == 'a' and y1 == 'b'):
        return

    x2, y2 = input_coor(input_x2, input_y2) 

    if (x2 == 'a' and y2 == 'b'):
        return

    add_line(x1, y1, x2, y2)


def add_line(x1, y1, x2, y2):
    global lines

    lines.append([x1, y1, x2, y2])

    ui.canv.create_line(x1, y1, x2, y2, fill='orange')


## функция для получения координат натыканных точек        
def input_points(event):
    global old_coor
    x = float(event.x)
    y = float(event.y)
    
    if old_coor == None:
        old_coor=([x,y])
    else:
        add_line(old_coor[0], old_coor[1], x, y)
        old_coor = None
    

## функция для тыканья отрезка
def input_points_canvas():
    ui.canv.bind('<Button - 1>', input_points)


## функция для ввода отсекателя с полей ввода
def input_rect(input_x1, input_y1, input_x2, input_y2):
    x1, y1 = input_coor(input_x1, input_y1)

    if (x1 == 'a' and y1 == 'b'):
        return

    x2, y2 = input_coor(input_x2, input_y2) 

    if (x2 == 'a' and y2 == 'b'):
        return

    global rect
    if rect != None:
        ui.canv.create_rectangle(rect[0], rect[1], rect[2], rect[3], outline='white')

    rect = [x1, y1, x2, y2]

    ui.canv.create_rectangle(x1, y1, x2, y2, outline='red')
    

def input_rect_bind(event):
    global rect
    if rect != None:
        ui.canv.create_rectangle(rect[0], rect[1], rect[2], rect[3], outline='white')

    global old_coor_rect

    x = float(event.x)
    y = float(event.y)
    
    if old_coor_rect == None:
        old_coor_rect=([x,y])
    else:
        rect = [old_coor_rect[0], old_coor_rect[1], x, y]
        ui.canv.create_rectangle(rect[0], rect[1], rect[2], rect[3], outline='red')
        old_coor_rect = None


## функция для тыканья отсекателя
def input_rect_canvas():
    ui.canv.bind('<Button - 1>', input_rect_bind)


## функция для очистки всего
def clean():
    ui.canv.delete("all")
    global lines, rect

    lines = []
    rect = None

## функция для получения кода точки
def get_code(x, y):
    global rect

    code = [0, 0, 0, 0]

    if x < rect[0]:
        code[0] = 1
    if x > rect[1]:
        code[1] = 1
    if y < rect[2]:
        code[2] = 1
    if y > rect[3]:
        code[3] = 1

    return code


def log_prod(code1, code2):
    p = 0
    for i in range(4):
        p += code1[i] & code2[i]

    return p


#  Видимость
def is_visible(line):
    """Видимость - 0 = невидимый
                   1 = видимый
                   2 = частично видимый"""

    # вычисление кодов концевых точек отрезка
    s1 = sum(get_code(line[0], line[1]))
    s2 = sum(get_code(line[2], line[3]))

    # предположим, что отрезок частично видим
    vis = 2

    # проверка полной видимости отрезка
    if not s1 and not s2:
        vis = VISIBLE
    else:
        # проверка тривиальной невидимости отрезка, тут либо тривиально невидим либо частично
        l = log_prod(get_code(line[0], line[1]), get_code(line[2], line[3]))
        if l != 0:
            vis = INVISIBLE

    return vis


## проверяем каждую линию
def cutoff_line(line):
    global rect

    # инициализация флага
    flag = 1 # общего положения
    t = 1

    # проверка вертикальности и горизонтальности отрезка
    if abs(line[2] - line[0]) < 1e-6:
        flag = -1   # вертикальный отрезок
    else:
        # вычисление наклона
        t = (line[3] - line[1]) / (line[2] - line[0])
        if abs(t) < 1e-6:
            flag = 0   # горизонтальный

    # для каждой стороны окна
    for i in range(4):
        vis = is_visible(line)
        if vis == VISIBLE:
            ui.canv.create_line(line[0], line[1], line[2], line[3], fill='green')
            return
        elif vis == INVISIBLE:
            return

        # проверка пересечения отрезка и стороны окна
        code1 = get_code(line[0], line[1])
        code2 = get_code(line[2], line[3])

        if code1[i] == code2[i]: ## и если так, то это ==0 и можно уходить, ибо точки пересечения нет
            ##так как если 1=1, то он тривиально невидимый
            continue

        # проверка нахождения Р1 вне окна; если Р1 внутри окна, то Р2 и Р1 поменять местами
        if code1[i] == 0:
            line[0], line[2] = line[2], line[0]
            line[1], line[3] = line[3], line[1]

        # поиск пересечений отрезка со сторонами окна
        # контроль вертикальности отрезка
        if flag != -1:
            if i < 2:
                line[1] = t * (rect[i] - line[0]) + line[1]
                line[0] = rect[i]
                continue
            else:
                line[0] = (1 / t) * (rect[i] - line[1]) + line[0]
        
        line[1] = rect[i]

    ui.canv.create_line(line[0], line[1], line[2], line[3], fill='green')


def cutoff():
    global lines, rect
    if rect == None:
        messagebox.showerror("Ошибка", "Не введен отсекатель")
        return

    if (len(lines) == 0):
        messagebox.showerror("Ошибка", "Не введены отрезки")
        return

    rect = [min(rect[0], rect[2]), max(rect[0], rect[2]), min(rect[1], rect[3]), max(rect[1], rect[3])]


    for line in lines:
        cutoff_line(line)
