from tkinter import *
from tkinter import messagebox
import time
import ui
from colormap import rgb2hex

points = []
edges = []
first_point = None
cur_point = None

pixel_state = []
EPS = 1e-6

flag_draw = 0
min_x = 0
max_x = 0
min_y = 0
max_y  = 0

seed_x = None
seed_y = None


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

## надфункция для считывания координат из полей ввода    
def add_point_input(input_x, input_y):
    x, y = input_coor(input_x, input_y)

    if (x == 'a' and y == 'b'):
        return

    add_point(x, y)

## функция для обновления таблицы
def update_table():
    ui.tb.config(state='normal')
    ui.tb.delete(0.0, END)
    ui.mytable.clear()

    const = round(ui.width_but/70)
    
    ui.mytable.field_names = [' '*const + '№' + ' '*const, ' '*const + 'X' + ' '*const, ' '*const + 'Y' + ' '*const]

    for i in range(len(points)):
        x = str(round(points[i][0], 2)) 
        y = str(round(points[i][1], 2))
        ui.mytable.add_row([str(i + 1), x, y])

    ui.tb.insert(INSERT, ui.mytable)
    ui.tb.config(state='disable')


## функция для получения координат натыканных точек        
def input_points(event):
    x = float(event.x)
    y = float(event.y)

    add_point(x, y)
    

## функция для добавления точки в таблицу
def add_point(x, y):
    global edges, points
    global cur_point, first_point

    points.append([x, y])

    if cur_point == None or first_point == None:
        cur_point = [x, y]
        first_point = [x, y]
        return

    edges.append([x,y, cur_point[0], cur_point[1]])
    cur_point = [x, y]
    # print(" edges ", edges)

    print_edges()
    update_table()

def sign(difference):
    if (difference < 0):
        return -1
    elif (difference == 0):
        return 0
    else:
        return 1

def bresenham_int(x1,y1,x2,y2, color):
    if (x2 - x1 == 0) and (y2 - y1 == 0):
        return [[x1, y1, color]]

    x = x1
    y = y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    s1 = sign(x2 - x1)
    s2 = sign(y2 - y1)

    if (dy > dx):
        tmp = dx
        dx = dy
        dy = tmp
        swaped = 1
    else:
        swaped = 0

    e = 2 * dy - dx
    i = 1

    while (i <= dx + 1):
        ui.image_canvas.put(color, (int(x), int(y)))

        while (e >= 0):
            if (swaped):
                x = x + s1
            else:
                y = y + s2

            e = e - 2 * dx

        if (swaped):
            y = y + s2
        else:
            x = x + s1

        e = e + 2 * dy
        i += 1


## функция для отрисовки ребер
def print_edges():
    global edges

    # ui.canv.delete("all")

    for i in range(len(edges)):
        x1 = edges[i][0]
        y1 = edges[i][1]

        x2 = edges[i][2]
        y2 = edges[i][3]

        bresenham_int(x1, y1, x2, y2,ui.const_line)
   
## замкнуть
def lock_edge():
    global edges
    global cur_point, first_point

    try:
        x1 = cur_point[0] 
        y1 = cur_point[1] 

        x2 = first_point[0]
        y2 = first_point[1]

        bresenham_int(x1, y1, x2, y2,ui.const_line)

        edges.append([x1, y1, x2, y2])

        cur_point = None
        first_point = None
    except:
        messagebox.showerror("Ошибка", "Нечего замыкать.")
        return

def input_seed_pixel(event):
    global seed_x, seed_y
    
    seed_x = float(event.x)
    seed_y = float(event.y)

    ui.canv.bind('<Button - 1>', input_points)


def touch_pixel_window():
    ui.canv.bind('<Button - 1>', input_seed_pixel)

## функция для тыканья точек
def input_points_canvas():
    ui.canv.bind('<Button - 1>', input_points)


## функция для очистки всего
def clean():
    ui.canv.delete("all")
    global points, edges
    global seed_x, seed_y
    global cur_point, first_point

    points = []
    edges = []

    seed_x = None
    seed_y = None

    cur_point = None
    first_point = None

    ui.tb.config(state='normal')
    ui.tb.delete(0.0, END)
    ui.tb.config(state='disable')

    ui.image_canvas = PhotoImage(width = ui.window.winfo_width(), height = ui.window.winfo_height())
    ui.canv.create_image((ui.window.winfo_width() / 2, ui.window.winfo_height() / 2), image = ui.image_canvas, state = "normal")

## функция для закрытие окошка
def exit_window(root):
    root.destroy()

## функция для добавления новой точки через поля ввода
def add_point_window():
    add_window=Tk()
    add_window.title('Добавление')
    add_window.geometry('350x150')

    text='Введите координаты точки:'
    input_center_lable=Label(add_window, font='Helvetica 12 bold', text = text, justify=LEFT).place(x=30, y=10)

    input_x_label=Label(add_window, font='Helvetica 12', text='X  =').place(x=30, y=52)
    input_x=Entry(add_window, width=7)
    input_x.place(x=80, y=50)

    input_y_label=Label(add_window, font='Helvetica 12', text='Y  =').place(x=210, y=52)
    input_y=Entry(add_window, width=7)
    input_y.place(x=260, y=50)

    add_button=Button(add_window, font='Helvetica 12', text='Добавить точку', command= lambda:add_point_input(input_x, input_y))
    add_button.place(x=80, y=100)

    exit_button=Button(add_window, font='Helvetica 12', text='Закрыть', command= lambda:exit_window(add_window))
    exit_button.place(x=250, y=100)

    input_x.insert(250,0)
    input_y.insert(250,0)

    add_window.mainloop()

def add_seed_pixel(input_x, input_y):
    global seed_x, seed_y

    x, y = input_coor(input_x, input_y)

    if (x == 'a' and y == 'b'):
        seed_x = None
        seed_y = None
        return

    seed_x = x
    seed_y = y

## функция для добавления затравки
def add_pixel_window():
    add_window=Tk()
    add_window.title('Ввод затравки')
    add_window.geometry('350x150')

    text='Введите координаты затравочной точки:'
    input_center_lable=Label(add_window, font='Helvetica 12 bold', text = text, justify=LEFT).place(x=10, y=10)

    input_x_label=Label(add_window, font='Helvetica 12', text='X  =').place(x=30, y=52)
    input_x=Entry(add_window, width=7)
    input_x.place(x=80, y=50)

    input_y_label=Label(add_window, font='Helvetica 12', text='Y  =').place(x=210, y=52)
    input_y=Entry(add_window, width=7)
    input_y.place(x=260, y=50)

    add_button=Button(add_window, font='Helvetica 12', text='Добавить затравку', command= lambda:add_seed_pixel(input_x, input_y))
    add_button.place(x=80, y=100)

    exit_button=Button(add_window, font='Helvetica 12', text='Закрыть', command= lambda:exit_window(add_window))
    exit_button.place(x=250, y=100)

    input_x.insert(250,0)
    input_y.insert(250,0)

    add_window.mainloop()


## ищем макс x, min y, max y чтоб докрашивать до правой границы фигуры  
def find_right_edge():
    global points
    global min_x, max_x, min_y, max_y

    max_x = points[0][0]
    min_x = points[0][0]
    min_y = points[0][1]
    max_y = points[0][1]

    for i in range(len(points)):
        if (points[i][0] < min_x):
            min_x = points[i][0]
        if (points[i][0] > max_x):
            max_x = points[i][0]
        if (points[i][1] > max_y):
            max_y = points[i][1]
        if (points[i][1] < min_y):
            min_y = points[i][1]

    max_x = int(max_x)
    min_x = int(min_x)
    max_y = int(max_y)
    min_y = int(min_y)


## изменение цвета пикселя
def fill_pixel(x, y):
    x = int(x)
    y = int(y)

    color = ui.image_canvas.get(x, y)
    color_hex = rgb2hex(color[0], color[1], color[2])
    color_hex = color_hex.lower()

    if (color_hex != ui.const_bg):
        ui.image_canvas.put(ui.const_draw, (x, y))
    else:
        ui.image_canvas.put(ui.const_bg, (x, y))
    
    if ui.is_delay.get() == 1:
        ui.canv.update()
        time.sleep(0.00005)


## алгоритм закрашивания
def fill_figure():
    global edges, EPS, flag_draw
    global seed_x, seed_y

    if (len(edges) < 3):
        messagebox.showerror("Ошибка", "Недостаточно ребер для закраски.")
        return

    if (seed_x == None or seed_y == None):
        messagebox.showerror("Ошибка", "Нет затравочного пикселя.")
        return


    bresenham_int(ui.window_size_X - 2, ui.window_size_Y, ui.window_size_X - 2, ui.window.winfo_height(), ui.const_line) ## |
    bresenham_int(ui.window_size_X - 2, ui.window_size_Y, ui.window.winfo_width(), ui.window_size_Y, ui.const_line) ## -

    bresenham_int(ui.window.winfo_width() - 2, ui.window_size_Y - 2, ui.window.winfo_width() - 2, ui.window.winfo_height(), ui.const_line)
    bresenham_int(ui.window_size_X - 2, ui.window.winfo_height() - 2, ui.window.winfo_width() -2, ui.window.winfo_height() - 2, ui.const_line)

    time_start = time.time()

    image_canvas = PhotoImage(width = ui.window.winfo_width(), height = ui.window.winfo_height())
    ui.canv.create_image((ui.window.winfo_width() / 2, ui.window.winfo_height() / 2), image = image_canvas, state = "normal")

        
    stack = list()
    stack.append((seed_x, seed_y))

    while (stack):
        dot_seed = stack.pop()

        x = int(dot_seed[0])
        y = int(dot_seed[1])
        ui.image_canvas.put(ui.const_draw, (x, y))

        tmp_x = x
        tmp_y = y

        # Заполнение текущей строки право до ребра или уже закрашенного пикселя
        x = x + 1

        color = ui.image_canvas.get(x, y)
        color_hex = rgb2hex(color[0], color[1], color[2])
        color_hex = color_hex.lower()

        while (color_hex != ui.const_line and color_hex != ui.const_draw):
            ui.image_canvas.put(ui.const_draw, (x, y))
            x = x + 1

            color = ui.image_canvas.get(x, y)
            color_hex = (rgb2hex(color[0], color[1], color[2])).lower()

        x_right = x - 1

        # Заполнение текущей строки влево до ребра или уже закрашенного пикселя
        x = tmp_x - 1

        color = ui.image_canvas.get(x, y)
        color_hex = rgb2hex(color[0], color[1], color[2])
        color_hex = color_hex.lower()

        while (color_hex != ui.const_line and color_hex != ui.const_draw):
            ui.image_canvas.put(ui.const_draw, (x, y))
            x = x - 1
            color = ui.image_canvas.get(x, y)
            color_hex = rgb2hex(color[0], color[1], color[2])
            color_hex = color_hex.lower()

        x_left = x + 1

        # Сканирование верхней строки
        x = x_left

        y = tmp_y + 1

        while (x <= x_right):
            flag = False

            color = ui.image_canvas.get(x, y)
            color_hex = rgb2hex(color[0], color[1], color[2])
            color_hex = color_hex.lower()

            # Поиск, есть ли в строке незакрашенный пиксель
            while (color_hex != ui.const_line 
            and color_hex != ui.const_draw 
            and x <= x_right):
                flag = True

                x = x + 1
                color = ui.image_canvas.get(x, y)
                color_hex = rgb2hex(color[0], color[1], color[2])
                color_hex = color_hex.lower()

            if (flag == True):
                color = ui.image_canvas.get(x, y)
                color_hex = rgb2hex(color[0], color[1], color[2])
                color_hex = color_hex.lower()

                if (x == x_right 
                        and color_hex != ui.const_line
                        and color_hex != ui.const_draw):
                    stack.append([x, y])
                else:
                    stack.append([x - 1, y])
            
                flag = False

            x_begin = x

            color = ui.image_canvas.get(x, y)
            color_hex = rgb2hex(color[0], color[1], color[2])
            color_hex = color_hex.lower()

            while ((color_hex == ui.const_line
            or color_hex == ui.const_draw)
            and x < x_right):
                x = x + 1

                color = ui.image_canvas.get(x, y)
                color_hex = rgb2hex(color[0], color[1], color[2])
                color_hex = color_hex.lower()

            if (x == x_begin):
                x = x + 1

        # Сканирование нижней строки
        x = x_left

        y = tmp_y - 1

        while (x <= x_right):
            flag = False    
            color = ui.image_canvas.get(x, y)
            color_hex = rgb2hex(color[0], color[1], color[2])
            color_hex = color_hex.lower()

            # Поиск, есть ли в строке незакрашенный пиксель
            while (color_hex!= ui.const_line
            and color_hex != ui.const_draw 
            and x <= x_right):
                flag = True

                x = x + 1
                color = ui.image_canvas.get(x, y)
                color_hex = rgb2hex(color[0], color[1], color[2])
                color_hex = color_hex.lower()

            if (flag == True):
                color = ui.image_canvas.get(x, y)
                color_hex = rgb2hex(color[0], color[1], color[2])
                color_hex = color_hex.lower()

                if (x == x_right 
                    and color_hex != ui.const_line
                    and color_hex!= ui.const_draw):
                    stack.append([x, y])
                else:
                    stack.append([x - 1, y])


                flag = False

            x_begin = x

            color = ui.image_canvas.get(x, y)
            color_hex = rgb2hex(color[0], color[1], color[2])
            color_hex = color_hex.lower()

            while ((color_hex == ui.const_line
                or color_hex == ui.const_draw)
            and x < x_right):
                x = x + 1

                color = ui.image_canvas.get(x, y)
                color_hex = rgb2hex(color[0], color[1], color[2])
                color_hex = color_hex.lower()

            if (x == x_begin):
                x = x + 1

        if ui.is_delay.get() == 1:
            ui.canv.update()
            # time.sleep(0.00000000005)
            time.sleep(0.005)

    
    time_end = time.time()
    text = "Время выполнения: " + str(round(time_end - time_start, 2))  + 'c'

    messagebox.showinfo("Время", text)
