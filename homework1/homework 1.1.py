#Задание 1. Форматирование строк
name = input("Ваше имя: ")
surname = input("Фамилия: ")
age = input("Возраст: ")

print("\nРеализация через format:")
print("Ваше имя: {}, Фамилия: {}, Возраст: {} лет".format(name, surname, age))

print("\nРеализация через f-string:")
print(f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет")

