#Задание 1. Возведение в степень
numbers = input("Введите числа через пробел: ").split()
power = int(input("Введите степень: "))
result = []

for element in numbers:
    if element.lstrip('-').isdigit():
        num = int(element)
        result.append(str(num ** power))
    else:
        result.append(element * power)

print("Вывод:", " ".join(result))

