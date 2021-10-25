#Задача 7. Яровенко Максим, ИУ5Ц-72Б

import json
import sys
import random

from lab_python_fp.cm_timer import *
from lab_python_fp.print_result import *
# Сделаем другие необходимые импорты



path = "D:\data_light.json"

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path, encoding='utf-8') as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    l = sorted(list(set(i['job-name'].capitalize() for i in arg)))
    return l



@print_result
def f2(arg):
    l = list(filter(lambda x: x.split()[0] == "Программист", arg))
    return l

@print_result
def f3(arg):
    l = list(map(lambda x: x + " с опытом Python", arg))
    return l

@print_result
def f4(arg):
    l = [", зарплата ".join(i) for i in list(zip(arg, [str(random.randint(100_000, 200_000)) for i in range(len(arg))]))]
    return l

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))

    input("Press Enter to continue...")
