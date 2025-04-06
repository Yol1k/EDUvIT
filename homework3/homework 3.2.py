def add(a: float, b: float):
    if not (isinstance(a, (int, float)) or not (isinstance(b, (int, float)))):
        raise TypeError("Оба аргумента должны быть числами")
    return a + b

def sub(a: float, b: float):
    if not (isinstance(a, (int, float)) or not (isinstance(b, (int, float)))):
        raise TypeError("Оба аргумента должны быть числами")
    return a - b

def mul(a: float, b: float):
    if not (isinstance(a, (int, float)) or not (isinstance(b, (int, float)))):
        raise TypeError("Оба аргумента должны быть числами")
    return a * b

def div(a: float, b: float, div_type: str):
    if not (isinstance(a, (int, float)) or not (isinstance(b, (int, float))) or not (isintance(div_type, int))):
        raise TypeError("Оба аргумента должны быть числами")
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    if div_type == "1":
        return a / b
    elif div_type == "2":
        return a // b
    elif div_type == "3":
        return a % b
    else:
        raise ValueError("Неверный тип деления. Допустимы: 1, 2, 3")

def power(a: float, b: float):
    if not (isinstance(a, (int, float)) or not (isinstance(b, (int, float)))):
        raise TypeError("Оба аргумента должны быть числами")
    if a == 0 and b < 0:
        raise ValueError("Ноль нельзя возводить в отрицательную степень")
    return a ** b

def fac(n: int):
    if not isinstance(n, int):
        raise TypeError("Аргумент должен быть целым числом")
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def avg(numbers: list[float]):
    return sum(numbers) / len(numbers)

def print_operations():
    print("Доступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Факториал")
    print("7. Среднее арифметическое")
    print("--------------------")

operations = {
    1: add,
    2: sub,
    3: mul,
    4: div,
    5: power,
    6: fac,
    7: avg
}
    
print_operations()
    
while True:
    try:
        operation = input("Операция: ")
        if operation in ('exit', 'quit', 'выход'):
            print("Завершение работы калькулятора")
            break

        operation = int(operation)
        if operation not in operations:
                    print("Неверный номер операции!")
                    continue
        if operation in (1, 2, 3, 5):
            a = float(input("Число 1: "))
            b = float(input("Число 2: "))
            result = operations[operation](a, b)
        elif operation == 4:
                a = float(input("Число 1: "))
                b = float(input("Число 2: "))
                div_type = input("Тип деления: (1) обычное (2) деление нацело (3) остаток от деления: ")
                result = operations[operation](a, b, div_type)
        elif operation == 6:
            n = int(input("Число: "))
            result = operations[operation](n)
        elif operation == 7:
            numbers = list(map(float, input("Список чисел: ").split()))
            result = operations[operation](numbers)
        print(f">>> {result}")
        print("--------------------")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except TypeError as e:
        print(f"Ошибка типа данных: {e}")
    except ZeroDivisionError as e:
        print(f"Математическая ошибка: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
