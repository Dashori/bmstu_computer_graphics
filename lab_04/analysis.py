import ui, draw, main
from tkinter import messagebox
import time, numpy
from math import pi, cos, sin, radians
import matplotlib.pyplot as plt

NUMBER_OF_RUNS = 20
MAX_RADIUS = 10000
STEP = 1000


def time_measure(option_figure):

    time_mes = []

    if (option_figure == 1):
        r_a = STEP
        r_b = r_a
        name = "окружность"
    else:
        r_a = STEP
        r_b = STEP
        name = "эллипс"

    dot_c = [800 // 2, 800 // 2]

    for i in range(1, 5):

        time_start = [0] * (MAX_RADIUS // STEP)
        time_end = [0] * (MAX_RADIUS // STEP)

        for _ in range(NUMBER_OF_RUNS):

            r_a = STEP
            r_b = STEP

            for k in range(MAX_RADIUS // STEP):
                rad = [r_a, r_b]
                
                time_start[k] += time.time()

                main.parse_methods(dot_c, rad, i, 4, option_figure, draw = False)

                time_end[k] += time.time()

                r_a += STEP
                r_b += STEP

        size = len(time_start)

        res_time = list((time_end[j] - time_start[j]) / NUMBER_OF_RUNS for j in range(size))

        time_mes.append(res_time)

        # clear_canvas()

    rad_arr = list(i for i in range(0, MAX_RADIUS, STEP))
    plt.figure(figsize = (14, 6))

    plt.title("Замеры времени для различных методов\nФигура: " + name)


    plt.plot(rad_arr, time_mes[0], label = "Каноническое\nуравнеие")

    plt.plot(rad_arr, time_mes[1], label = "Параметрическое\nуравнение")

    plt.plot(rad_arr, time_mes[2], label = "Брезенхем")

    plt.plot(rad_arr, time_mes[3], label = "Алгоритм\nсредней точки")


    plt.xticks(numpy.arange(STEP, MAX_RADIUS, STEP))
    plt.legend()

    plt.ylabel("Время")
    plt.xlabel("Величина радиуса")

    plt.show()
