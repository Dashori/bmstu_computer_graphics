
from tkinter import *
import main, draw, analysis

const_bg = "#ffffff"
const_draw = (0,0,0)

window_size_X = 800
window_size_Y = 800

window=Tk()
window.title('Lab 4 Chepigo Darya IU7-44B')
window.geometry('1400x1000')

def config(event):
    if event.widget == window:
        global window_size_X, window_size_Y

        window_size_X=window.winfo_width()/800
        window_size_Y=window.winfo_height()/800

        canv.place(x=250*window_size_X, y=40*window_size_Y-10, width=530*window_size_X, height=700*window_size_Y)

        ## условие
        task_button.place(x=400*window_size_X, y=750*window_size_Y, width=120*window_size_X, height=30*window_size_Y)

        ## о программе
        info_button.place(x=540*window_size_X, y=750*window_size_Y, width=120*window_size_X, height=30*window_size_Y)

        ##очистить канву
        clean_canvas_but.place(x=250*window_size_X, y=750*window_size_Y, width=120*window_size_X, height=30*window_size_Y)

        ## выход 
        exit_button.place(x=680*window_size_X, y=750*window_size_Y, width=100*window_size_X, height=30*window_size_Y)

        ## методы
        alg_choose_label.place(x=40, y=30)
 
        method_canon.place(x=30, y=70)
        method_param.place(x=30, y=105)
        method_bresenhem.place(x=30, y=140)
        method_middle_point.place(x=30, y=175)
        method_biblio.place(x=30, y=205)

        ## выбор фигуры
        choose_figure_label.place(x=40, y=245)

        circle_but.place(x=30, y=275)
        ellipse_but.place(x=230, y=275)

        ## фигура
        draw_figure_label.place(x=40, y=320)

        coordinate_new_label_xc.place(x=25*window_size_X, y=300*window_size_Y)
        coordinate_new_label_yc.place(x=130*window_size_X, y=300*window_size_Y)

        add_point_entry_xc.place(x=57*window_size_X, y=297*window_size_Y, width=50*window_size_X, height=22*window_size_Y)
        add_point_entry_yc.place(x=162*window_size_X, y=297*window_size_Y, width=50*window_size_X, height=22*window_size_Y)

        draw_figure_but.place(x=40, y=455, width=185*window_size_X, height=27*window_size_Y)

        ## спектр

        spectrum_label.place(x=40, y=500)

        step_label.place(x=25*window_size_X, y=460*window_size_Y)
        count_label.place(x=130*window_size_X, y=460*window_size_Y)

        step.place(x=57*window_size_X, y=457*window_size_Y, width=50*window_size_X, height=22*window_size_Y)
        count.place(x=162*window_size_X, y=457*window_size_Y,width=50*window_size_X, height=22*window_size_Y)

        draw_spectrum_but.place(x=40, y=650, width=185*window_size_X, height=27*window_size_Y)
        
        ## изменение цвета
        
        color_bg.place(x=40, y=700, width=185*window_size_X, height=30*window_size_Y)
        color_draw.place(x=40, y=750, width=185*window_size_X, height=30*window_size_Y)

        ##сравнение

        compare_time_lab.place(x=40, y=800, width=185*window_size_X, height=30*window_size_Y)
        compare_gradation_lab.place(x=40, y=850, width=185*window_size_X, height=30*window_size_Y)

        change_figure(choose_figure_but.get())
        change_state(extra.get())

        
              
window.bind("<Configure>", config)
canv = Canvas(window, bg = "white")


def change_state(option):
    if (option==1):
        step.config(state='readonly')
        count.config(state='normal')
        spectrum_radius_start_entry.config(state='normal')
        spectrum_radius_end_entry.config(state='normal')
    elif (option==2):
        step.config(state='normal')
        count.config(state='readonly')
        spectrum_radius_start_entry.config(state='normal')
        spectrum_radius_end_entry.config(state='normal')
    elif (option==3):
        step.config(state='normal')
        count.config(state='normal')
        spectrum_radius_start_entry.config(state='readonly')
        spectrum_radius_end_entry.config(state='normal')
    elif (option==4):
        step.config(state='normal')
        count.config(state='normal')
        spectrum_radius_start_entry.config(state='normal')
        spectrum_radius_end_entry.config(state='readonly')

    

## изменение канвы в зависимости от фигуры
def change_figure(option):
    if (option==1): ##окружность
        radius_1_label.place_forget()
        radius_2_label.place_forget()
        radius_1_entry.place_forget()
        radius_2_entry.place_forget()
        spectrum_radius_1_label.place_forget()
        spectrum_radius_2_label.place_forget()
        spectrum_radius_1_entry.place_forget()
        spectrum_radius_2_entry.place_forget()

        change_state(extra.get())

        radius_label.place(x=25*window_size_X, y=350*window_size_Y)
        radius_entry.place(x=57*window_size_X, y=347*window_size_Y, width=50*window_size_X, height=22*window_size_Y)

        spectrum_radius_start_label.place(x=25*window_size_X, y=510*window_size_Y)
        spectrum_radius_end_label.place(x=130*window_size_X, y=510*window_size_Y)

        spectrum_radius_start_entry.place(x=57*window_size_X, y=507*window_size_Y, width=50*window_size_X, height=22*window_size_Y)
        spectrum_radius_end_entry.place(x=162*window_size_X, y=507*window_size_Y, width=50*window_size_X, height=22*window_size_Y)

        extra_step.place(x=5*window_size_X, y=457*window_size_Y)
        extra_n.place(x=110*window_size_X, y=457*window_size_Y)
        extra_r_start.place(x=5*window_size_X, y=507*window_size_Y) 
        extra_r_end.place(x=110*window_size_X, y=507*window_size_Y)

    elif (option==2):
        radius_label.place_forget()
        radius_entry.place_forget()
        spectrum_radius_start_label.place_forget()
        spectrum_radius_end_label.place_forget()
        spectrum_radius_start_entry.place_forget()
        spectrum_radius_end_entry.place_forget()
        extra_step.place_forget()
        extra_n.place_forget()
        extra_r_start.place_forget()
        extra_r_end.place_forget()

        step.config(state='normal')
        count.config(state='normal')

        radius_1_label.place(x=25*window_size_X, y=350*window_size_Y)
        radius_2_label.place(x=130*window_size_X, y=350*window_size_Y)

        radius_1_entry.place(x=57*window_size_X, y=347*window_size_Y, width=50*window_size_X, height=22*window_size_Y)
        radius_2_entry.place(x=162*window_size_X, y=347*window_size_Y, width=50*window_size_X, height=22*window_size_Y)

        spectrum_radius_1_label.place(x=25*window_size_X, y=510*window_size_Y)
        spectrum_radius_2_label.place(x=130*window_size_X, y=510*window_size_Y)

        spectrum_radius_1_entry.place(x=57*window_size_X, y=507*window_size_Y, width=50*window_size_X, height=22*window_size_Y)
        spectrum_radius_2_entry.place(x=162*window_size_X, y=507*window_size_Y, width=50*window_size_X, height=22*window_size_Y)
       

##
## Выбор алгоритма
##

alg_choose_label=Label(text='Выберите алгоритм построения:', font = 'Helvetica 14 bold')

option=IntVar()
option.set(1)

method_canon = Radiobutton(text = "Каноническое уравнение", font="-family {Helvetica} -size 14", variable = option, value = 1)
method_param = Radiobutton(text = "Параметрическое уравнение", font="-family {Helvetica} -size 14", variable = option, value = 2)
method_bresenhem = Radiobutton(text = "Алгоритм Брезенхема", font="-family {Helvetica} -size 14", variable = option, value = 3) 
method_middle_point = Radiobutton(text = "Алгоритма средней точки", font="-family {Helvetica} -size 14", variable = option, value = 4) 
method_biblio = Radiobutton(text = "Библиотечная функция", font="-family {Helvetica} -size 14", variable = option, value = 5)


##
## Выбрать цвет фона
##

color_bg=Button(text='Выбрать цвет фона',font = 'Helvetica 14 bold', command = lambda: main.change_bg())


##
## Выбрать цвет рисования
##

color_draw=Button(text='Выбрать цвет для отрисовки',font = 'Helvetica 14 bold',  command = lambda: main.change_draw())

##
## Выбор фигуры
##

choose_figure_label=Label(text='Выберите фигуру:', font = 'Helvetica 14 bold')

choose_figure_but=IntVar()
choose_figure_but.set(1)

circle_but = Radiobutton(text = "Окружность", font="-family {Helvetica} -size 14", variable = choose_figure_but,
value=1, command=lambda: change_figure(choose_figure_but.get()))

ellipse_but = Radiobutton(text = "Эллипс", font="-family {Helvetica} -size 14", variable = choose_figure_but,
value=2, command=lambda: change_figure(choose_figure_but.get()))


##
## Построение фигуры
##

draw_figure_label=Label(text='Построение фигуры', font = 'Helvetica 14 bold')

coordinate_new_label_xc=Label(font='Helvetica', text='Xс    =')
coordinate_new_label_yc=Label(font='Helvetica', text='Yс    =')

add_point_entry_xc=Entry(font='Helvetica')
add_point_entry_yc=Entry(font='Helvetica')


radius_label=Label(font='Helvetica', text='R    =')
radius_entry=Entry(font='Helvetica')

radius_1_label=Label(font='Helvetica', text='R_1   =')
radius_2_label=Label(font='Helvetica', text='R_2   =')

radius_1_entry=Entry(font='Helvetica')
radius_2_entry=Entry(font='Helvetica')

draw_figure_but=Button(text='Построить фигуру',font = 'Helvetica 14 bold',
 command = lambda: draw.create_segment(option.get(), const_draw))


# add_point_entry_xn.insert("end", "-100")
# add_point_entry_yn.insert("end", "-100")

# add_point_entry_xk.insert("end", "50")
# add_point_entry_yk.insert("end", "100")

##
## Построение спектра
##

spectrum_label=Label(text='Построение спектра',font = 'Helvetica 14 bold')

count_label=Label(font='Helvetica', text='N      =')
step_label=Label(font='Helvetica', text='Шаг  =')

count=Entry(font='Helvetica')
step=Entry(font='Helvetica')

draw_spectrum_but=Button(text='Построить спектр',font = 'Helvetica 14 bold', 
command= lambda: draw.parse_spektr(option.get(), const_draw))

## для эллипса
spectrum_radius_1_label=Label(font='Helvetica', text='R_1   =')
spectrum_radius_2_label=Label(font='Helvetica', text='R_2   =')

spectrum_radius_1_entry=Entry(font='Helvetica')
spectrum_radius_2_entry=Entry(font='Helvetica')

## для окружности
spectrum_radius_start_label=Label(font='Helvetica', text='R_start')
spectrum_radius_end_label=Label(font='Helvetica', text='R_end')

spectrum_radius_start_entry=Entry(font='Helvetica')
spectrum_radius_end_entry=Entry(font='Helvetica')

## выбор лишнего параметра
extra=IntVar()
extra.set(1)

extra_step = Radiobutton(variable = extra, value = 1, command=lambda: change_state(extra.get()))
extra_n = Radiobutton(variable = extra, value = 2, command=lambda: change_state(extra.get()) )
extra_r_start = Radiobutton(variable = extra, value = 3, command=lambda: change_state(extra.get())) 
extra_r_end = Radiobutton(variable = extra, value = 4, command=lambda: change_state(extra.get()))



# len.insert("end", "10")
# step.insert("end", "250")


##
## Сравнить время
##

compare_time_lab=Button(font='Helvetica 14 bold', text='Сравнить время', command= lambda: analysis.time_measure())

##
## Сравнить ступенчатость
##

compare_gradation_lab=Button(font='Helvetica 14 bold', text='Сравнить ступенчатость', command= lambda: analysis.steps_measure()) 

##
## Очистить канвас
##

clean_canvas_but=Button(font='Helvetica 14 bold', text = 'Очистить канвас', command= lambda: canv.delete("all"))

##
## Инфо и условие
##

task_button=Button(font='Helvetica 14 bold', text = 'Условие', command= lambda: main.task_programm())

info_button=Button(font='Helvetica 14 bold', text = 'О программе', command= lambda: main.info_programm())


##
## Выход
##

exit_button=Button(font='Helvetica 14 bold', text='Выход', command= lambda: window.destroy())

window.mainloop()
