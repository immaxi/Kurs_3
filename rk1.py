#РИП. РК1. Яровенко Максим, ИУ5Ц-72Б. Вариант Б27

from operator import itemgetter

class Prepod:
    """Преподаватель"""
    def __init__(self, id, fio, sal, kurs_id):
        self.id = id                                    #id записи
        self.fio = fio                                  #фамилия преподавателя
        self.sal = sal                                  #зарплата преподавателя
        self.kurs_id = kurs_id                          #id курса

class Kurs:
    """Учебный курс"""
    def __init__(self, id, name):
        self.id = id                                    #id курса
        self.name = name                                #название курса

class PrepodKurs:
    """'Преподавтели курса' для реализации связи многое-ко-многим"""
    def __init__(self, p_id, k_id):
        self.p_id = p_id
        self.k_id = k_id

#Учебные курсы
kurses = [
    Kurs(1, "Информатика"),
    Kurs(2, "Основы программирования"),
    Kurs(3, "Электроника"),
    Kurs(4, "Базы данных"),
    Kurs(5, "Разработка интернет-приложений"),
    Kurs(6, "БКИТ")
    ]


#Преподаватели
prepods = [
    Prepod(1, "Козлов", 20000, 2),
    Prepod(2, "Правдина", 30000, 1),
    Prepod(3, "Белодедов", 40000, 3),
    Prepod(4, "Ревунков", 30000, 4),
    Prepod(5, "Ковалева", 20000, 4),
    Prepod(6, "Гапанюк", 80000, 6),
    Prepod(7, "Канев", 80000, 5),
    ]

#Реализация связим многое-ко-многим
prepod_kurses = [
    PrepodKurs(1, 1),
    PrepodKurs(1, 2),
    PrepodKurs(2, 1),
    PrepodKurs(2, 2),
    PrepodKurs(3, 3),
    PrepodKurs(4, 4),
    PrepodKurs(5, 4),
    PrepodKurs(6, 5),
    PrepodKurs(6, 6),
    PrepodKurs(7, 5),
    PrepodKurs(7, 6),
    ]

def main():
    """Основная функция"""

    #Соединение данных один-ко-многим
    one_to_many = [(p.fio, p.sal, k.name)
                   for k in kurses
                   for p in prepods
                   if p.kurs_id == k.id
                   ]

    #Соединение данных многое-ко-многим
    many_to_many_temp = [(t.p_id, k.name)
                         for k in kurses
                         for t in prepod_kurses
                         if t.k_id == k.id
                         ]
    many_to_many = [(p.fio, p.sal, name)
                    for p_id, name in many_to_many_temp
                    for p in prepods 
                    if p.id == p_id
                    ]

    #Задание Б1. Один-ко-многим. Вывести список всех связанных преподавателей
    # и учебных курсов, отсортированный по преподавателям
    print("Задание Б1")
    res_1 = sorted(one_to_many, key = itemgetter(0))
    print(res_1)

    #Задание Б2. Один-ко-многим. Вывести список учебных курсов с количеством
    # преподавателей, ведущих каждый курс. Сортировка по количеству преподавателей 
    print("\nЗадание Б2")

    res_2 = []
    for k in kurses:
        count_prepod = 0
        for p in prepods:
            if p.kurs_id == k.id:
                count_prepod += 1
        res_2.append((k.name, count_prepod))
    res_2 = sorted(res_2, key = itemgetter(1), reverse = True)
    print(res_2)

    #Задание Б3. Многое-ко-многим. Вывести список всех преподавателей, у которых
    # фамилия заканчивается на "ов", а также те учебные курсы, которые они ведут 
    print("\nЗадание Б3")
    sort_prepod = list(filter(lambda x: x[0][-2:] == "ов", many_to_many))
    
    res_3 = {}
    while len(sort_prepod)>0:
        fio = sort_prepod[0][0]
        sp = list(filter(lambda x: x[0] == fio, many_to_many))
        res_3[sp[0][0]] = [x for _,_,x in sp]
        for i in sort_prepod:
            if i[0] == fio:
                sort_prepod.remove(i)
    print(res_3)

if __name__ == "__main__":
    main()