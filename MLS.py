import math
import numpy as np

# MLS for linear function
def linear_MLS(x, y):
    length = len(y)

    y_ = sum(y) / len(x)
    x_ = sum(x) / len(y)

    s1 = 0
    s2 = 0

    for i in range(length):
        s1 += (x[i] - x_) * (y[i] - y_)
        s2 += (x[i] - x_) ** 2

    m = s1 / s2
    b = y_ - m * x_

    result = 'y = ' + str(m) + '* x + ' + str(b)

    av_sc = 0
    for i in range(length):
        av_sc += (y[i] - (m * x[i])) ** 2

    av_sc = math.sqrt(av_sc / length)

    max_x = max(x)
    min_x = min(x)
    dots_per_draw = 100
    step = (min_x + max_x) / dots_per_draw

    drawing_data_x = np.arange(min_x, max_x, step)
    drawing_data_y = [m * drawing_data_x[i] + b for i in drawing_data_x]

    draw_data = [drawing_data_x, drawing_data_y]

    return result, av_sc, draw_data

# MSL for exponential function
def exp_MLS(x, y):
    length = len(x)

    x2y = 0
    ylny = 0
    xy = 0
    xylny = 0
    sumy = 0

    for i in range(length):
        x2y += (x[i] ** 2) * y[i]
        ylny += y[i] * math.log(y[i], math.e)
        xy += x[i] * y[i]
        xylny += x[i] * y[i] * math.log(y[i], math.e)
        sumy += y[i]

    a = (x2y * ylny - xy * xylny) / (sumy * x2y - (xy) ** 2)

    b = (sumy * xylny - xy * ylny) / (sumy * x2y - (xy) ** 2)

    flag = 1
    sa = 0
    for i in range(len(str(a))):
        if flag == 0:
            sa += 1
        if str(a)[i] == '.':
            flag = 0

    flag = 1
    sb = 0
    for i in range(len(str(a))):
        if flag == 0:
            sb += 1
        if str(a)[i] == '.':
            flag = 0

    a = a * (10 ** sa)

    result = str(round(a, 3)) + ' * 10ˆ(' + str(sa) + ")" + '* eˆ( x * ' + str(round(b, 3)) + '* 10ˆ(' + str(
        sb) + '))'

    av_sc = 0
    for i in range(length):
        av_sc += (y[i] - (a * math.e ** (x[i] * b))) ** 2

    av_sc = math.sqrt(av_sc / length)

    max_x = max(x)
    min_x = min(x)
    dots_per_draw = 100
    step = (min_x + max_x) / dots_per_draw

    drawing_data_x = np.arange(min_x, max_x, step)
    drawing_data_y = [a * (math.e ** (x[i] * b)) for i in drawing_data_x]

    draw_data = [drawing_data_x, drawing_data_y]

    return result, av_sc, draw_data

# MSL for parabolic function
def parab_MLS(x, y):
    length = len(x)

    s4 = 0
    s3 = 0
    s2 = 0
    s1 = 0
    s11 = 0
    s21 = 0
    s01 = 0

    for i in range(length):
        s4 += x[i] ** 4
        s3 += x[i] ** 3
        s2 += x[i] ** 2
        s1 += x[i]
        s01 += y[i]
        s11 += x[i] * y[i]
        s21 += y[i] * (x[i] ** 2)

    rigth_matrix = np.array([s21, s11, s01])
    left_matrix = np.array([[s4, s3, s2], [s3, s2, s1], [s2, s1, 1]])
    left_matrix = left_matrix.transpose()
    coef_matrix = rigth_matrix * left_matrix

    a = coef_matrix[0]
    b = coef_matrix[1]
    c = coef_matrix[2]

    av_sc = 0

    for i in range(length):
        av_sc += ((a * (x[i] ** 2) + b * x[i] + c) - y[i]) ** 2

    av_sc = math.sqrt(av_sc / length)

    result = "y = " + str(a) + " * xˆ2 + " + str(b) + " * x" + str(c)

    max_x = max(x)
    min_x = min(x)
    dots_per_draw = 100
    step = (min_x + max_x) / dots_per_draw

    drawing_data_x = np.arange(min_x, max_x, step)
    drawing_data_y = [a* (x[i] ** 2 + b * x[i] ++ c) for i in drawing_data_x]

    draw_data = [drawing_data_x, drawing_data_y]

    return result, av_sc, draw_data

# MSL for function a + b * ln(x)
def blnx_MSL(x, y):
    length = len(x)

    sy = 0
    sy_x = 0
    slnx = 0
    slnx_x = 0
    s1_x = 0

    for i in range(length):
        sy += y[i]
        sy_x += y[i] / x[i]
        s1_x += 1 / x[i]
        slnx += math.log(x[i], math.e)
        slnx_x += (math.log(x[i], math.e))

    rigth_matrix = np.array([sy, sy_x])
    left_matrix = np.array([[length, slnx],
                            [s1_x, slnx_x]])

    left_matrix = left_matrix.transpose()

    ab_matrix = left_matrix * rigth_matrix

    a = ab_matrix[0]
    b = ab_matrix[1]

    av_sc = 0
    for i in range(length):
        av_sc += (a + b * math.log(x[i], math.e) - y[i]) ** 2

    av_sc = math.sqrt(av_sc / length)

    result = "y = " + str(a) + " + " + str(b) + " * ln(x)"

    max_x = max(x)
    min_x = min(x)
    dots_per_draw = 100
    step = (min_x + max_x) / dots_per_draw

    drawing_data_x = np.arange(min_x, max_x, step)
    drawing_data_y = [a + b * math.log(x[i], math.e) for i in drawing_data_x]

    draw_data = [drawing_data_x, drawing_data_y]

    return result, av_sc, draw_data

# MSL for function a * xˆb
def ax_b_MSL(x, y):
    length = len(x)

    lnx = 0
    lny = 0
    lnx_2 = 0
    lnxlny = 0

    for i in range(length):
        lnx += math.log(x[i], math.e)
        lny += math.log(y[i], math.e)
        lnx_2 += math.log(x[i], math.e) ** 2
        lnxlny += (math.log(x[i], math.e)) * (math.log(y[i], math.e))

    b = (length * lnxlny - lnx * lny) / (length * lnx_2 - (lnx) ** 2)
    a = (lny - b * lnx) / length
    a = math.e ** a

    av_sc = 0

    for i in range(length):
        av_sc += (a * (x[i] ** b) - y[i]) ** 2

    av_sc = math.sqrt(av_sc / length)

    result = "y = " + str(a) + " * xˆ(" + str(b) + ")"

    max_x = max(x)
    min_x = min(x)
    dots_per_draw = 100
    step = (min_x + max_x) / dots_per_draw

    drawing_data_x = np.arange(min_x, max_x, step)
    drawing_data_y = [a + x[i] ** b for i in drawing_data_x]

    draw_data = [drawing_data_x, drawing_data_y]

    return result, av_sc, draw_data

# Summarisation of MSL for different functions
# And fingind the best one

# Actually user should to use only this one
def MLS(x, y):
    res = [linear_MLS(x, y), exp_MLS(x, y), parab_MLS(x, y), blnx_MSL(x, y), ax_b_MSL(x, y)]
    p = min(res[0][1], res[1][1], res[2][1], res[3][1], res[4][1])
    result = "Something wrong"
    draw_data = []
    for i in range(len(res)):
        if res[i][1] == p:
            result = res[i][0]
            draw_data = res[3]

    return result, draw_data
