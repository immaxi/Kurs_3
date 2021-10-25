#Программа для решения биквадратного уравнения. Яровенко Максим, ИУ5Ц-72Б

def get_coef(index, text):
    try:
        coef = sys.argv(index) 
    except:
        coef = input(text)
    try:
        coef = float(coef)
    except:
        print("Введено не число, повторите попытку")
        coef = get_coef(index, text)
    return coef


print("Программа решает биквадратное уравнение вида Ax^4 + Bx^2 + C = 0")

a = get_coef(1, "Введите коэффициент А: ")
b= get_coef(2, "Введите коэффициент B: ")
c = get_coef(3, "Введите коэффициент C: ")

result = []
d = b*b - 4*a*c
if d == 0:
    y = -b/(2*a)
    if y == 0:
        result.append(0)
    elif y > 0:
        result.append(-(y**0.5))
        result.append(y**0.5)
elif d > 0:
    y1 = (-b - d**0.5) / (2*a)
    y2 = (-b + d**0.5) / (2*a)
    if y1 == 0:
        result.append(0)
    elif y1 > 0:
        result.append(-(y1**0.5))
        result.append(y1**0.5)
    if y2 == 0:
        result.append(0)
    elif y2 > 0:
        result.append(-(y2**0.5))
        result.append(y2**0.5)
if len(result) == 0:
    print("Корней нет")
elif len(result) == 1:
    print(f"Один корень: {result[0]}")
elif len(result) == 2:
    print(f"Два корня: {result[0]}, {result[1]}")
elif len(result) == 3:
    print(f"Четыре корня: {result[0]}, {result[1]}, {result[2]}")

else:
    print(f"Четыре корня: {result[0]}, {result[1]}, {result[2]}, {result[3]}")

input("Нажмите Enter для продолжения")