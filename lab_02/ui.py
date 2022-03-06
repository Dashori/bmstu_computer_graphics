
from tkinter import *
import func
import draw

window=Tk()
window.title('Lab 2 Chepigo Darya IU7-44B')
window.geometry('800x800')

def config(event):
    if event.widget == window:

        window_size_X=window.winfo_width()/800
        window_size_Y=window.winfo_height()/800
        print(window_size_X)
        ## смасштабирорвать
        scale_button.place(x=400*window_size_X, y=30*window_size_Y, width=170*window_size_X, height=30*window_size_Y)

        ## перемместить
        transfer_button.place(x=100*window_size_X, y=30*window_size_Y, width=120*window_size_X, height=30*window_size_Y)

        ## повернуть
        rotate_button.place(x=250*window_size_X, y=30*window_size_Y, width=120*window_size_X, height=30*window_size_Y)

        ## шаг назад 
        back_button.place(x=580*window_size_X, y=30*window_size_Y, width=120*window_size_X, height=30*window_size_Y)

        ## о программе
        info_button.place(x=550*window_size_X, y=750*window_size_Y, width=120*window_size_X, height=30*window_size_Y)

        ## выход 
        exit_button.place(x=680*window_size_X, y=750*window_size_Y, width=100*window_size_X, height=30*window_size_Y)

        draw.const_x = draw.const * window_size_X
        draw.text_x = draw.const_x

        draw.const_y = draw.const * window_size_Y
        draw.text_y = draw.const_y

        draw.index_cutoff_x = int(draw.const_x / draw.const_cutoff)
        draw.index_cutoff_y = int(draw.const_y / draw.const_cutoff)

        draw.center_x=draw.const_x - 200
        draw.center_y=draw.const_y - 270

        draw.print_rabbit()

        canv.place(x=80*window_size_X, y=100*window_size_Y, width=650*window_size_X, height=650*window_size_Y)

        
window.bind("<Configure>", config)

##
## Изменение масштаба
##


scale_button=Button(font='Helvetica 12 bold', text = 'Изменить масштаб')

##
## Перенос изображения
##

transfer_button=Button(font='Helvetica 12 bold', text = 'Переместить')


##
## Поворот изображения
##

rotate_button=Button(font='Helvetica 12 bold', text = 'Повернуть', command= lambda: draw.rotate_window())

##
## Шаг назад
##

back_button=Button(font='Helvetica 12 bold', text = 'Шаг назад') #, command= lambda: pass;ui_func.back())

##
## Инфо
##

info_button=Button(font='Helvetica 12 bold', text = 'О программе', command= lambda: func.info_programm())


##
## Выход
##

exit_button=Button(font='Helvetica 12 bold', text='Выход', command= lambda: window.destroy())


# canv = Canvas(window, bg = "light grey")
canv = Canvas(window, bg = "white")

# draw.print_rabbit()
# draw.print_arrows()
window.mainloop()
