from tkinter import *
import ui_func
import func

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

def draw_circle():
    window = Tk()
    window.title('Points')
    window.geometry('800x800')

    canv = Canvas(window, width = 800, height = 800, bg = "light grey")
    canv.create_line(400,800,400,0,width=2,arrow=LAST,) 
    canv.create_line(0,400,800,400,width=2,arrow=LAST) 

    for i in range(ui_func.count):
        x = (ui_func.points[i][0] + 400) 
        y = (ui_func.points[i][1] + 400) 
        canv.create_oval(x, y, x + 5, y + 5, fill = 'black')
    canv.create_oval(func.need_point_1[0] + 400, func.need_point_1[1] + 400, func.need_point_1[0] + 405, func.need_point_1[1] + 405, fill = 'red')
    
    canv.create_oval(func.x - func.radius + 400, func.y + func.radius + 400, func.x + func.radius + 400, func.y - func.radius + 400, outline = 'red')    

    canv.pack()	
    window.resizable(width=False, height=False)
    window.mainloop()