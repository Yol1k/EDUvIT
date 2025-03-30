#Задание 2. Четность числа
digit = input("Введите число: ")
if digit.isdigit():
    digit = int(digit)
    if digit >= 0:
        if digit % 2 == 0:
            print(f"Число {digit} является чётным")
        else:
            print(f"Число {digit} не является чётным")
else:
    print("Ошибка: введено не число")
