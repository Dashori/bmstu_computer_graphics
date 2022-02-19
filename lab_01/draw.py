from tkinter import *
import ui_func
import ui
import func

const = 300
const_x = 300
const_y = 300
const_circle = 290
const_cutoff = 50

def print_arrows():
    ui.canv.create_line(const_x, const_y * 2, const_x,0,width=2,arrow=LAST) 
    ui.canv.create_line(0,const_y,const_x * 2,const_y,width=2,arrow=LAST)

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
    

    ## x +
    for line in range(int(const_x), int(const_x) * 2, const_cutoff):
        text_plus = int((line - const_x))

        if (text_plus == 0):
            ui.canv.create_text(line + 10, const_y - 10, 
            text=str(text_plus), justify=LEFT, font=('Helvetica 10'))
            continue

        ui.canv.create_text(line - 10, const_y - 10, 
        text=str(text_plus), justify=LEFT, font=('Helvetica 10'))
    ## x-
    for line in range(int(const_x), 0, -const_cutoff):
        text_plus = int((line - const_x))

        ui.canv.create_text(line + 10, const_y - 10, 
        text=str(int(text_plus)), justify=LEFT, font=('Helvetica 10'))


    ## y+
    for line in range(int(const_y), int(const_y) * 2, const_cutoff):
        
        text = -int((line - const_y))
        if (text == 0):
            continue

        ui.canv.create_text(const_x - 20, line, 
        text=str(text), justify=LEFT, font=('Helvetica 10'))
    ## y-
    for line in range(int(const_y), 0, -const_cutoff):
        
        text = -int((line - const_y))
        if (text == 0):
            continue

        ui.canv.create_text(const_x - 20, line, 
        text=str(text), justify=LEFT, font=('Helvetica 10'))

        
def input_points(event):
    x = event.x
    y = event.y

    print(x,y)

    ui.canv.create_oval(x - 2.5, y - 2.5, x + 2.5, y + 2.5)
    ui_func.add_point(float(x) - const_x, (-1)*(float(y) - const_y))
    

def input_points_canvas():
    ui.canv.bind('<Button - 1>', input_points)
    print_arrows()

    
def print_res_text():
    ui.solve_text.config(state='normal')
    ui.solve_text.delete(0.0, END)

    text_1 = 'Построена окружность с радуисом ' + str(round(func.radius,2)) + '\n'
    text_1 += 'Проходящяя через точки \n(' + str(round(func.need_point_1[0],2)) + ',' + str(round(func.need_point_1[1],2)) + ')\n'
    text_1 += '(' + str(round(func.need_point_2[0],2)) + ',' + str(round(func.need_point_2[1],2)) + ')\n'
    text_1 += '(' + str(round(func.need_point_3[0],2)) + ',' + str(round(func.need_point_3[1],2)) + ')\n'
    text_1 += 'И с центром в точке (' + str(round(func.x,2)) + ',' + str(round(func.y,2)) + ')'
    ui.solve_text.insert(INSERT, text_1)
    ui.solve_text.config(state='disable')


def print_points():
    ui.canv.delete("all")

    for i in range(ui_func.count):
        x = ui_func.points[i][0] + const_x
        y = (-1)*(ui_func.points[i][1]) + const_y
        ui.canv.create_oval(x - 2.5, y - 2.5, x + 2.5, y + 2.5, fill = 'red')
    print_arrows()

    # if (func.radius > 0):
    #     text = "print('!')"
    #     ui_func.back_command.append(text)

def print_circle_canva():
    text = "func.find_min_circle()"
    ui_func.back_command.append(text)

    print_points()
    if (func.radius > 0):
        ui.canv.create_oval(func.x - func.radius + const, -func.y - func.radius + const, func.x + func.radius + const, -func.y + func.radius + const, outline = 'red')


def draw_circle():
    ui.canv.delete("all")
    print_points()

    ## точка с наим расстоянием до неё
    ui.canv.create_oval(func.need_point_1[0] + const_x - 2.5, (-1)*(func.need_point_1[1]) + const_y - 2.5,
    func.need_point_1[0] + const_x + 2.5, (-1)*(func.need_point_1[1]) + const_y + 2.5, fill = 'blue')

    ## окружность
    ui.canv.create_oval(func.x - func.radius + const_x, (-1)*(func.y) + func.radius + const_y,
    func.x + func.radius + const_x, (-1)*(func.y) - func.radius + const_y, outline = 'red')

    ## центр окружности
    ui.canv.create_oval(func.x  + const_x, (-1)*(func.y) + const_y,
    func.x + 5 + const_x, (-1)*(func.y) + 5 + const_y, fill = 'green')

    print_res_text()
    scaling()

def fix_points(new_point, radius):

    ## перенос окружности в центр 0 0 
    x = (new_point[0] - func.x)* (const_circle)/const_x
    y = ((-1)*new_point[1] - (-1)*func.y) 

    x = round(x,2)
    y = round(y,2)
    ui.canv.create_oval(x - 2.5 + const_x, y - 2.5 + const_y, x + 2.5 + const_x, y + 2.5 + const_y, fill = 'red')
    # print(x,y)

    ## растяжение окружности на большую с радиусом 300
    new_point_1 = [(x * const_circle)/func.radius, (y * const_circle)/func.radius] 

    ui.canv.create_oval(new_point_1[0] - 2.5 + const_x , new_point_1[1] - 2.5 + const_y,
    new_point_1[0] + 2.5 + const_x, new_point_1[1] + 2.5 + const_y, fill = 'blue')

    text = '(' + str(round(new_point[0],2)) + ',\n' + str(round(new_point[1],2)) + ')'
    ui.canv.create_text(new_point_1[0] + const_circle, new_point_1[1] + const_circle, text = text)

    ui.canv

    return new_point


def scaling():

    ui.canv.delete("all")
    difference_x = func.x 
    difference_y = (-1)*func.y

    # radius = 300
    fix_points(func.need_point_1, const_circle)
    fix_points(func.need_point_2, const_circle)
    fix_points(func.need_point_3, const_circle) 

    ui.canv.create_oval(func.x - const_circle + const_x - difference_x, (-1)*(func.y) + const_circle + const_y - difference_y,
    func.x + const_circle + const_x - difference_x, (-1)*(func.y) - const_circle + const_y - difference_y, outline = 'black')

    ui.canv.create_oval(-2.5  + const_x, -2.5 + const_y,
    2.5 + const_x, 2.5 + const_y, fill = 'green')

    text = '(' + str(round(func.x,2)) + ',' + str(round(func.y,2)) + ')'

    ui.canv.create_text(const_circle - 10, const_circle - 10, text = text)

