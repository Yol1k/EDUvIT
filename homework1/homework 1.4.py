#Задание 4. Длина числа
while True:
    user_input = input("Введите число: ")
    
    if user_input == "exit":
        print("Выход из программы...")
        break
    
    if user_input.lstrip('-').isdigit():
        num_length = len(user_input.lstrip('-'))
        if num_length == 1:
            print(f"В этом числе {num_length} цифра")
        elif num_length > 1 and num_length < 5:
            print (f"В этом числе {num_length} цифры")
        else:
            print (f"В этом числе {num_length} цифр")
    else:
        print("Ошибка: данные не являются числом.")
