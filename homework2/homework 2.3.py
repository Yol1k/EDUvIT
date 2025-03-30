#Задание 3. Пересечение двух списков
list1 = list(map(int, input("Введите первый список: ").split()))
list2 = list(map(int, input("Введите второй список: ").split()))

list3 = set(list1) & set(list2)
print("Общие элементы:", " ".join(map(str, list3)))
