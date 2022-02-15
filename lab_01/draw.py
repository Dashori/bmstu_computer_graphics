from ctypes.wintypes import PINT
from os import stat
from tkinter import *
import ui_func
import ui
import func

const = 320

def print_arrows():
    ui.canv.create_line(const,const * 2,const,0,width=2,arrow=LAST) 
    ui.canv.create_line(0,const,const * 2,const,width=2,arrow=LAST)

    for line in range(0, const * 2, 80):
        ui.canv.create_line([(line, const - 4), (line, const + 4)], width = 3, fill='black')
    
    for line in range(0, const * 2, 80):
        ui.canv.create_line([(const - 4, line), (const + 4,line)], width = 3, fill='black')

    for line in range(0, const * 2, 80):
        ui.canv.create_text(line - 15,const - 10, 
        text=str(line - const), justify=LEFT, font=('Helvetica 10'))
        
        ui.canv.create_text(const - 15,line - 10, 
        text=str((-1)*(line - const)), justify=LEFT, font=('Helvetica 10'))
        
        
def input_points(event):
    x = event.x
    y = event.y

    print(x,y)

    ui.canv.create_oval(x - 2.5, y - 2.5, x + 2.5, y + 2.5)
    ui_func.add_point(float(x) - const, (-1)*(float(y) - const))
    

def input_points_canvas():
    ui.canv.bind('<Button - 1>', input_points)
    print_arrows()

    
def print_res_text():
    ui.solve_text.config(state='normal')

    # ui.solve_text.delete(0,'end')

    text_1 = 'Построена окружность с радуисом ' + str(round(func.radius,2)) + '\n'
    text_1 += 'Проходящяя через точки \n(' + str(func.need_point_1[0]) + ',' + str (func.need_point_1[1]) + ')\n'
    text_1 += '(' + str(func.need_point_2[0]) + ',' + str (func.need_point_2[1]) + ')\n'
    text_1 += '(' + str(func.need_point_3[0]) + ',' + str (func.need_point_3[1]) + ')\n'
    text_1 += 'И с центром в точке (' + str(round(func.x,2)) + ',' + str(round(func.y,2)) + ')'
    ui.solve_text.insert(INSERT, text_1)
    # ui.solve_text.insert('end', text_2)

    # ui.solve_text.config(state='disable')



def print_points():
    ui.canv.delete("all")
    for i in range(ui_func.count):
        x = (ui_func.points[i][0] + const) 
        y = (-1)*(ui_func.points[i][1]) + const
        ui.canv.create_oval(x - 2.5, y - 2.5, x + 2.5, y + 2.5, fill = 'red')
    print_arrows()


def draw_circle():
    ui.canv.delete("all")
    print_points()
    
    ## точка с наим расстоянием до неё
    ui.canv.create_oval(func.need_point_1[0] + const - 2.5, (-1)*(func.need_point_1[1]) + const - 2.5,
    func.need_point_1[0] + const + 2.5, (-1)*(func.need_point_1[1]) + const + 2.5, fill = 'blue')

    ## окружность
    ui.canv.create_oval(func.x - func.radius + const, (-1)*(func.y) + func.radius + const,
    func.x + func.radius + const, (-1)*(func.y) - func.radius + const, outline = 'red')

    ## центр окружности
    ui.canv.create_oval(func.x  + const, (-1)*(func.y) + const,
    func.x + 5 + const, (-1)*(func.y) + 5 + const, fill = 'green')

    print_res_text()
    scaling()

def fix_points(new_point, radius):

    ## перенос окружности в центр 0 0 
    x = (new_point[0] - func.x ) 
    y = ((-1)*new_point[1] - (-1)*func.y) 

    # ui.canv.create_oval(x - 2.5 + const, y - 2.5 + const, x + 2.5 + const, y + 2.5 + const, fill = 'red')
    # print(x,y)

    ## растяжение окружности на большую с радиусом 300
    new_point_1 = [(x * radius)/func.radius, (y * radius)/func.radius] 

    ui.canv.create_oval(new_point_1[0] - 2.5 + const , new_point_1[1] - 2.5 + const,
    new_point_1[0] + 2.5 + const, new_point_1[1] + 2.5 + const, fill = 'blue')

    text = '(' + str(new_point[0]) + ',\n' + str(new_point[1]) + ')'
    ui.canv.create_text(new_point_1[0] + const, new_point_1[1] + const, text = text)

    ui.canv

    return new_point


def scaling():

    ui.canv.delete("all")
    difference_x = func.x 
    difference_y = (-1)*func.y

    radius = 300
    fix_points(func.need_point_1, radius)
    fix_points(func.need_point_2, radius)
    fix_points(func.need_point_3, radius) 

    ui.canv.create_oval(func.x - radius + const - difference_x, (-1)*(func.y) + radius + const - difference_y,
    func.x + radius + const - difference_x, (-1)*(func.y) - radius + const - difference_y, outline = 'black')

    ui.canv.create_oval(-2.5  + const, -2.5 + const,
    2.5 + const, 2.5 + const, fill = 'green')

    text = '(' + str(round(func.x,2)) + ',' + str(round(func.y,2)) + ')'

    ui.canv.create_text(const - 10, const - 10, text = text)

    
