#Задача 1. Яровенко Максим, ИУ5Ц-72Б

def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        sl = ""
        for k in items:
            if k[args[0]] != None:
               sl = str(k[args[0]])
               yield sl
    elif len(args) > 1:
        sl = {}
        for k in items:
            for i in range(len(args)):
                if k[args[i]] != None:
                    sl[args[i]] = k[args[i]]
            yield sl
            sl.clear()



goods = [
    {'title': 'Диван', 'price': 2000, 'color': 'Черный'},
    {'title': 'Кресло','price': 500, 'color': 'Красный'},
    {'title': 'Утюг','price': 1000, 'color': None},
    {'title': 'Картина','price': 1500, 'color': None},
    {'title': 'Стол','price': None, 'color': None}    
    ]

print("Генератор field(goods, 'title'):")
for i in field(goods, 'title'):
    print(i)

print("\nГенератор field(goods, 'price'):")
for i in field(goods, 'price'):
    print(i)

print("\nГенератор field(goods,  'title', 'price'):")
for i in field(goods, 'title', 'price'):
    print(i)

print("\nГенератор field(goods,  'title', 'color'):")
for i in field(goods, 'title', 'color'):
    print(i)

input("Press Enter to continue...")


