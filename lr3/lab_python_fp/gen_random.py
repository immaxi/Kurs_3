#Задача 2. Яровенко Максим, ИУ5Ц-72Б

from random import randint

def gen_random(kolvo, min, max):                           #генератор 
    for k in range(kolvo):
        i = randint(min, max)
        yield i

data = gen_random(15, 1, 10)
for i in data:                            #пример работы генератора
    print(i)

input("Press Enter to continue...")

