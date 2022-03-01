from tkinter import *
from tkinter import messagebox
import ui_func
import ui
import func

const = 300
const_x = 300
const_y = 300
const_circle = 280
const_cutoff = 50
index_cutoff_x = 6
index_cutoff_y = 6

text_y = 300
text_x = 300

flag_canva = 0

def round_numbers(num):
    if (num < 5):
        num = round(num,2)
    else:
        num = int(num)
    return num

def print_arrows():
    ui.canv.create_line(const_x, const_y * 2, const_x,0, width=2,arrow=LAST) 
    ui.canv.create_line(0, const_y, const_x * 2, const_y, width=2,arrow=LAST)

    ## x
    for line in range(int(const_x), int(const_x) * 2 , const_cutoff):
        ui.canv.create_line([(line, int(const_y) - 4), (line, int(const_y) + 4)], width = 3, fill='black')
    for line in range(int(const_x), 0, -const_cutoff):
        ui.canv.create_line([(line, int(const_y) - 4), (line, int(const_y) + 4)], width = 3, fill='black')
    ## y
    for line in range(int(const_y), int(const_y) * 2, const_cutoff):
        ui.canv.create_line([(int(const_x) - 4, line), (int(const_x) + 4,line)], width = 3, fill='black')
    for line in range(int(const_y), 0, -const_cutoff):
        ui.canv.create_line([(int(const_x) - 4, line), (int(const_x) + 4,line)], width = 3, fill='black')

    global text_x

    ## текст x
    text_points_x = []
    for i in range(1, index_cutoff_x + 2):
        x = text_x * i/(index_cutoff_x)
        text_points_x.append(round_numbers(x))
        
    ## текст y
    text_points_y = []
    for i in range(1,index_cutoff_y + 2):
        y = text_y * i/(index_cutoff_y)
        text_points_y.append(round_numbers(y))
    point_text = -2

    ## x +
    for line in range(int(const_x), int(const_x) * 2, const_cutoff):
        point_text += 1
        if (point_text == -1):
            ui.canv.create_text(line + 10, const_y - 10, 
            text=str(0), justify=LEFT, font=('Helvetica 10'))
            continue

        ui.canv.create_text(line - 10, const_y - 10, 
        text=str(text_points_x[point_text]), justify=LEFT, font=('Helvetica 10'))
        
    ## x-
    point_text = -2
    for line in range(int(const_x), 0, -const_cutoff):
        point_text += 1
        if (point_text == -1):
            continue

        ui.canv.create_text(line + 10, const_y - 10, 
        text=str((-1) * text_points_x[point_text]), justify=LEFT, font=('Helvetica 10'))


    ## y+
    point_text = -2
    for line in range(int(const_y), int(const_y) * 2, const_cutoff):
        point_text += 1
        if (point_text == -1):
            continue

        ui.canv.create_text(const_x - 20, line, 
        text=str((-1) * text_points_y[point_text]), justify=LEFT, font=('Helvetica 10'))

    ## y-
    point_text = -2
    for line in range(int(const_y), 0, -const_cutoff):
        point_text += 1
        if (point_text == -1):
            continue

        ui.canv.create_text(const_x - 20, line, 
        text=str(text_points_y[point_text]), justify=LEFT, font=('Helvetica 10'))

        
def input_points(event):
    x = event.x
    y = event.y

    x = (float(x) - const_x) * text_x / const_x 
    y = (-1)*(float(y) - const_y) * text_y / const_y
    ui_func.add_point(x, y)
    

def input_points_canvas():
    ui.canv.bind('<Button - 1>', input_points)
    print_arrows()

    
def print_res_text():
    ui.solve_text.config(state='normal')
    ui.solve_text.delete(0.0, END)

    text_1 = 'Построена окружность с радуисом ' + str(round(func.radius,2)) + '\n'
    text_1 += 'Проходящяя через точки \n(' + str(round(func.need_point_1[0],2)) + ',' + str(round(func.need_point_1[1],2)) + ') (синяя)\n'
    text_1 += '(' + str(round(func.need_point_2[0],2)) + ',' + str(round(func.need_point_2[1],2)) + ')\n'
    text_1 += '(' + str(round(func.need_point_3[0],2)) + ',' + str(round(func.need_point_3[1],2)) + ')\n'
    text_1 += 'И с центром в точке (' + str(round(func.x,2)) + ',' + str(round(func.y,2)) + ')'
    ui.solve_text.insert(INSERT, text_1)
    ui.solve_text.config(state='disable')


def back_solve():
    print_points()
    ui.solve_text.config(state='normal')
    ui.solve_text.delete(0.0, END)
    ui.solve_text.config(state='disable')
    text = "print('!') "
    ui_func.back_command.append(text)

    ui.scale_plus_button['state'] = 'normal'
    ui.scale_minus_button['state'] = 'normal'


def print_points():
    ui.canv.delete("all")

    for i in range(ui_func.count):
        x = ui_func.points[i][0] * const_x / text_x + const_x
        y = (-1)*(ui_func.points[i][1]) * const_y / text_y + const_y
        ui.canv.create_oval(x - 2.5, y - 2.5, x + 2.5, y + 2.5, fill = 'red')
    print_arrows()


def print_circle_canva():
    global flag_canva
    flag_canva = 1
    func.flag = 0

    if (func.radius < 0):
        messagebox.showerror("Ошибка", "Вы уже на канве.")
        return

    text = "func.find_min_circle()"
    ui_func.back_command.append(text)

    print_points()
    x = func.need_point_1[0] * const_x / text_x + const_x
    y = (-1)*func.need_point_1[1] * const_y / text_y + const_y
    ui.canv.create_oval(x - 2.5, y - 2.5, x + 2.5, y + 2.5, fill = 'blue')

    if (func.radius > 0):
        x1 =  (func.x - func.radius) * const_x / text_x + const_x 
        x2 =  (func.x + func.radius) * const_x / text_x + const_x

        y1 = (-func.y - func.radius) * const_y / text_y + const_y 
        y2 = (-func.y + func.radius) * const_y / text_y + const_y 
        ui.canv.create_oval(x1, y1, x2, y2, outline = 'red')

        x3 = func.x * const_x / text_x + const_x 
        y3 = (-1)*(func.y) * const_y / text_y + const_y 
        ui.canv.create_oval(x3, y3, x3 + 5, y3 + 5, fill = 'green')

    ui.scale_plus_button['state'] = 'normal'
    ui.scale_minus_button['state'] = 'normal'


def draw_circle():
    ui.canv.delete("all")
    print_points()

    ## точка с наим расстоянием до неё
    x1 = func.need_point_1[0] * const_x / text_x + const_x  
    y1 = (-1)*(func.need_point_1[1]) * const_y / text_y + const_y 

    ui.canv.create_oval(x1 - 2.5, y1 - 2.5,
    x1 + 2.5, y1 + 2.5, fill = 'blue')

    x2 = (func.x - func.radius) * const_x / text_x + const_x 
    y2 = (-func.y - func.radius) * const_y / text_y + const_y 

    x3 = (func.x + func.radius) * const_x / text_x + const_x
    y3 = (-func.y + func.radius) * const_y / text_y + const_y 

    ## окружность
    ui.canv.create_oval(x2, y2, x3, y3, outline = 'red')

    # ## центр окружности
    x4 = func.x * const_x / text_x + const_x 
    y4 = (-1)*(func.y) * const_y / text_y + const_y 
    ui.canv.create_oval(x4, y4, x4 + 5, y4 + 5, fill = 'green')

    print_res_text()


def fix_points(new_point, color):

    ## перенос окружности в центр 0 0 
    x = (new_point[0] - func.x)
    y = ((-1)*new_point[1] - (-1)*func.y) 

    x = round(x,2)
    y = round(y,2)

    ## растяжение окружности на большую с радиусом 300
    new_point_1 = [(x * const_circle)/func.radius, (y * const_circle)/func.radius] 

    ui.canv.create_oval(new_point_1[0] - 2.5 + const_x , new_point_1[1] - 2.5 + const_y,
    new_point_1[0] + 2.5 + const_x, new_point_1[1] + 2.5 + const_y, fill = color)

    text = '(' + str(round(new_point[0],2)) + ',\n' + str(round(new_point[1],2)) + ')'
    ui.canv.create_text(new_point_1[0] - 5 + const_x, new_point_1[1] - 5 + const_y, text = text)

    return new_point


def scaling_circle():
    ui.canv.delete("all")
    difference_x = func.x 
    difference_y = (-1)*func.y

    # отрисовка точек в зависимости от радиуса окружности
    fix_points(func.need_point_1, "blue")
    fix_points(func.need_point_2, "red")
    fix_points(func.need_point_3, "red") 

    x2 = (func.x - func.radius)  + const_x 
    y2 = (-func.y - func.radius) + const_y 

    x3 = (func.x + func.radius)  + const_x
    y3 = (-func.y + func.radius)  + const_y 

    ## окружность

    ui.canv.create_oval(func.x - const_circle + const_x - difference_x, (-1)*(func.y) + const_circle + const_y - difference_y,
    func.x + const_circle + const_x - difference_x, (-1)*(func.y) - const_circle + const_y - difference_y, outline = 'black')

    ui.canv.create_oval(-2.5  + const_x, -2.5 + const_y,
    2.5 + const_x, 2.5 + const_y, fill = 'green')

    text = '(' + str(round(func.x,2)) + ',' + str(round(func.y,2)) + ')'

    ui.canv.create_text(const_x - 10, const_y - 10, text = text)

    ui.scale_plus_button['state'] = 'disabled'
    ui.scale_minus_button['state'] = 'disabled'