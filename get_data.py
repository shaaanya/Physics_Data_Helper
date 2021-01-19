from openpyxl import *
from physics_data_helper.exp_data import *
import math


def get_data(road_to_file, colomn_with_x, colomn_with_y, start_line, finish_line, sheet_number=0):
    wb = load_workbook(filename=road_to_file, data_only=True)

    name = road_to_file.split("/")
    name = name[len(name)]
    name = name.split(".")
    name = name[0]

    sheet_names = wb.get_sheet_names()

    sheet = wb.get_sheet_by_name(sheet_names[sheet_number])

    x_list = []
    y_list = []

    for i in range(start_line, finish_line + 1, 1):
        x_list.append(sheet[colomn_with_x + str(i)].value)
        y_list.append(sheet[colomn_with_y + str(i)].value)

    return x_list, y_list, name


def err(x, sys_err):
    length = len(x)

    s = 0
    av = sum(x) / length

    for i in range(length):
        s += (x[i] - av) ** 2

    random_error = math.sqrt(s) / length

    absolute_error = sys_err + random_error
    relative_error = absolute_error / av

    result = (absolute_error, relative_error)

    return result


def error(x, y, system_error):
    x_res = err(x, system_error)
    y_res = err(y, system_error)

    for i in range(len(x)):
        x[i] = Experiment_data(x[i], x_res[0], x_res[1])
        y[i] = Experiment_data(y[i], y_res[0], y_res[1])

    return x, y
