#Задача 4. Яровенко Максим, ИУ5Ц-72Б

def sorter(item):
    return abs(item)

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

print("Реализация сортировки без lambda-функции:")
result = sorted(data, reverse = True, key = sorter)
print(result)

print("\nРеализация сортировки с lambda-функцией:")
result_with_lambda = sorted(data, reverse = True, key = lambda item: abs(item))
print(result_with_lambda)

input("Press Enter to continue...")