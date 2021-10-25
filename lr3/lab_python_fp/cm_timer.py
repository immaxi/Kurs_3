#Задача 6. Яровенко Максим, ИУ5Ц-72Б

import time
from contextlib import contextmanager

class cm_timer_1:

    def __enter__(self):
        self.time1 = time.perf_counter()
        
        return None
        
    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            
            self.time2 =time.perf_counter()
            print ("time:", self.time2-self.time1)

@contextmanager
def cm_timer_2():
    time1 = time.perf_counter()
    yield None
    time2 = time.perf_counter()
    print ("time:", time2-time1)

if __name__ == '__main__':
    print("Демонстрация работы контекстного менеджера, реализованного на основе класса:")
    with cm_timer_1():
        time.sleep(3)

    print("\nДемонстрация работы контекстного менеджера, реализованного с использованием библиотеки contextlib:")
    with cm_timer_2():
        time.sleep(5)

    input("Press Enter to continue...")

