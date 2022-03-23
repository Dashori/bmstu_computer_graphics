
from tkinter import *
import ui_func, draw

const_bg = "#ffffff"
const_draw = (0,0,0)

window=Tk()
window.title('Lab 3 Chepigo Darya IU7-44B')
window.geometry('1400x1000')

def config(event):
    if event.widget == window:

        window_size_X=window.winfo_width()/800
        window_size_Y=window.winfo_height()/800

        ## условие
        task_button.place(x=400*window_size_X, y=750*window_size_Y, width=120*window_size_X, height=30*window_size_Y)

        ## о программе
        info_button.place(x=540*window_size_X, y=750*window_size_Y, width=120*window_size_X, height=30*window_size_Y)

        ##очистить канву
        clean_canvas_but.place(x=250*window_size_X, y=750*window_size_Y, width=120*window_size_X, height=30*window_size_Y)

        ## выход 
        exit_button.place(x=680*window_size_X, y=750*window_size_Y, width=100*window_size_X, height=30*window_size_Y)

        canv.place(x=250*window_size_X, y=40*window_size_Y - 10, width=530*window_size_X, height=700*window_size_Y)

        ## методы
        alg_choose_label.place(x=40, y = 30)

        method_wu.place(x=300, y=105)
        method_cda.place(x=300, y=70)
        method_bresenhem_float.place(x=30, y = 70)
        method_bresenhem_int.place(x=30, y = 105)
        method_bresenhem_smooth.place(x=30, y = 140)


        ## отрезок
        draw_segment_lab.place(x=40, y=300)

        coordinate_new_label_xn.place(x=25 * window_size_X, y=300*window_size_Y)
        coordinate_new_label_yn.place(x=120 * window_size_X, y=300*window_size_Y)

        add_point_entry_xn.place(x=55 * window_size_X, y=300*window_size_Y, width=50 * window_size_X)
        add_point_entry_yn.place(x=150 * window_size_X, y=300*window_size_Y, width=50 * window_size_X)


        coordinate_new_label_xk.place(x=25 * window_size_X, y=350*window_size_Y)
        coordinate_new_label_yk.place(x=120 * window_size_X, y=350*window_size_Y)

        add_point_entry_xk.place(x=55 * window_size_X, y=350*window_size_Y, width=50 * window_size_X)
        add_point_entry_yk.place(x=150 * window_size_X, y=350*window_size_Y, width=50 * window_size_X)


        draw_segment_but.place(x=40, y=480)

        ##пучок

        draw_bundle_lab.place(x=40, y=550)

        b_coordinate_new_label_xn.place(x=25 * window_size_X, y=510*window_size_Y)
        b_coordinate_new_label_yn.place(x=120 * window_size_X, y=510*window_size_Y)

        b_add_point_entry_xn.place(x=55 * window_size_X, y=510*window_size_Y, width=50 * window_size_X)
        b_add_point_entry_yn.place(x=160 * window_size_X, y=510*window_size_Y, width=50 * window_size_X)


        b_step_lab.place(x=25 * window_size_X, y=560*window_size_Y)
        b_len_lab.place(x=120 * window_size_X, y=560*window_size_Y)

        b_len.place(x=55 * window_size_X, y=560*window_size_Y, width=50 * window_size_X)
        b_step.place(x=160 * window_size_X, y=560*window_size_Y, width=50 * window_size_X)

        draw_bundle_but.place(x=40, y=730)

        ##сравнение

        compare_time_lab.place(x=40, y= 800)

        compare_gradation_lab.place(x=40, y= 860)


        color_bg.place(x=40, y=200)
        color_draw.place(x=40, y=250)

 
        
window.bind("<Configure>", config)

##
## Изменение масштаба
##

canv = Canvas(window, bg = "white")


# colorchooser.askcolor()
       

##
## Выбор алгоритма
##

alg_choose_label= Label(text='Выберите алгоритм построения:', font = 'Helvetica 12 bold')

option = IntVar()
option.set(1)

method_cda = Radiobutton(text = "ЦДА", font="-family {Helvetica} -size 14", variable = option, value = 1)
method_wu = Radiobutton(text = "Ву", font="-family {Helvetica} -size 14", variable = option, value = 4)
method_bresenhem_float = Radiobutton(text = "Брезенхем (float)", font="-family {Helvetica} -size 14", variable = option, value = 3) 
method_bresenhem_int = Radiobutton(text = "Брезенхем (int)", font="-family {Helvetica} -size 14", variable = option, value = 2) 
method_bresenhem_smooth = Radiobutton(text = "Брезенхем (сглаживание)", font="-family {Helvetica} -size 14", variable = option, value = 5)

##
## Выбрать цвет фона
##

color_bg=Button(text='Выбрать цвет фона',font = 'Helvetica 14 bold', command = lambda: ui_func.change_bg())


##
## Выбрать цвет рисования
##

color_draw=Button(text='Выбрать цвет для отрисовки',font = 'Helvetica 14 bold',  command = lambda: ui_func.change_draw())

##
## Построение отрезка
##

draw_segment_lab=Label(text='Построение одиночного отрезка',font = 'Helvetica 14 bold')

coordinate_new_label_xn=Label(font='Helvetica', text='Xn     =')
coordinate_new_label_yn=Label(font='Helvetica', text='Yn     =')

add_point_entry_xn=Entry(font='Helvetica')
add_point_entry_yn=Entry(font='Helvetica')

coordinate_new_label_xk=Label(font='Helvetica', text='Xk     =')
coordinate_new_label_yk=Label(font='Helvetica', text='Yk     =')

add_point_entry_xk=Entry(font='Helvetica')
add_point_entry_yk=Entry(font='Helvetica')

draw_segment_but=Button(text='Построить отрезок',font = 'Helvetica 14 bold',
 command = lambda: draw.create_segment(option.get(), const_draw))


add_point_entry_xn.insert("end", "-100")
add_point_entry_yn.insert("end", "-100")

add_point_entry_xk.insert("end", "50")
add_point_entry_yk.insert("end", "100")

##
## Построение пучка
##

draw_bundle_lab=Label(text='Построение пучка отрезков',font = 'Helvetica 14 bold')

b_coordinate_new_label_xn=Label(font='Helvetica', text='Xc     =')
b_coordinate_new_label_yn=Label(font='Helvetica', text='Yc        =')

b_add_point_entry_xn=Entry(font='Helvetica')
b_add_point_entry_yn=Entry(font='Helvetica')

b_len_lab=Label(font='Helvetica', text='Длина  =')
b_step_lab=Label(font='Helvetica', text='Шаг  =')

b_len=Entry(font='Helvetica')
b_step=Entry(font='Helvetica')

draw_bundle_but=Button(text='Построить пучок',font = 'Helvetica 14 bold', 
command= lambda: draw.parse_spektr(option.get(), const_draw))


b_add_point_entry_xn.insert("end", "100")
b_add_point_entry_yn.insert("end", "100")
b_len.insert("end", "30")
b_step.insert("end", "300")


##
## Сравнить время
##

compare_time_lab=Button(font='Helvetica 14 bold', text='Сравнить время')


##
## Сравнить ступенчатость
##

compare_gradation_lab=Button(font='Helvetica 14 bold', text='Сравнить ступенчатость')



##
## Очистить канвас
##

clean_canvas_but=Button(font='Helvetica 14 bold', text = 'Очистить канвас', command= lambda: canv.delete("all"))


##
## Инфо
##

task_button=Button(font='Helvetica 14 bold', text = 'Условие', command= lambda: ui_func.task_programm())

info_button=Button(font='Helvetica 14 bold', text = 'О программе', command= lambda: ui_func.info_programm())


##
## Выход
##

exit_button=Button(font='Helvetica 14 bold', text='Выход', command= lambda: window.destroy())


# canv = Canvas(window, bg = "light grey")


window.mainloop()
