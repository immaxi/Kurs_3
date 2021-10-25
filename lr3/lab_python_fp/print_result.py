#Задача 5. Яровенко Максим, ИУ5Ц-72Б

def print_result(func):

    def other_func(*args, **kwargs):
        print(func.__name__)
        vozvrat = func(*args, **kwargs)
        if type(vozvrat) == list:
            for i in vozvrat:
                print(i)
        elif type(vozvrat) == dict:
            for k, v in vozvrat.items():
                print(k, " = ", v)
        else:
            print(vozvrat)
        return func(*args, **kwargs)
            
    return other_func


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]

if __name__ == '__main__':
    print("Демонстрация работы декоратора")
    test_1()
    test_2()
    test_3()
    test_4()

    input("Press Enter to continue...")