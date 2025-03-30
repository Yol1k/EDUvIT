#Задание 2. Преобразование словаря
dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

keys_set = set(dct.keys())
values_set = set(dct.values())

print("Множество ключей:", keys_set)
print("Множество значений:", values_set)
print("Объединение множеств:", keys_set | values_set)
