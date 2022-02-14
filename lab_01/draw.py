from tkinter import *
import ui_func
import ui
import func

const = 320

def draw_points():
    window = Tk()
    window.title('Points')
    window.geometry('800x800')

    canv = Canvas(window, width = 800, height = 800, bg = "light grey")
    canv.create_line(400,800,400,0,width=2,arrow=LAST,) 
    canv.create_line(0,400,800,400,width=2,arrow=LAST) 

    for i in range(ui_func.count):
        x = ui_func.points[i][0] + 400
        y = ui_func.points[i][1] + 400
        canv.create_oval(x, y, x + 5, y + 5, fill = 'black')

    canv.pack()	
    window.resizable(width=False, height=False)
    window.mainloop()

def print_arrows():
    ui.canv.create_line(320,640,320,0,width=2,arrow=LAST) 
    ui.canv.create_line(0,320,640,320,width=2,arrow=LAST) 

def input_points(event):
    x = event.x
    y = event.y

    print(x,y)

    ui.canv.create_oval(x, y, x + 5, y + 5)
    ui_func.add_point(float(x) - const, (-1)*(float(y) - const))
    

def input_points_canvas():
    ui.canv.bind('<Button - 1>', input_points)
    print_arrows()
    
def draw_circle():

    for i in range(ui_func.count):
        x = (ui_func.points[i][0] + const) 
        y = (-1)*(ui_func.points[i][1] + const) 
        ui.canv.create_oval(x, y, x + 5, y + 5, fill = 'black')
    ui.canv.create_oval(func.need_point_1[0] + const, (-1)*(func.need_point_1[1]) + const, func.need_point_1[0] + const + 5, (-1)*(func.need_point_1[1]) + const + 5, fill = 'red')
    
    ui.canv.create_oval(func.x - func.radius + const, (-1)*(func.y) + func.radius + const, func.x + func.radius + const, (-1)*(func.y) - func.radius + const, outline = 'red')    

    ui.canv.create_oval(func.x  + const, (-1)*(func.y) + const, func.x + 5 + const, (-1)*(func.y) + 5 + const, fill = 'green')