def func(nums: list[int], mn: int = 2):
    list1 = [num * mn for num in nums]
    return list1

lambda_func = lambda list2, mn=2: list(map(lambda x: x * mn, list2))

list3 = input("Введите список чисел через пробел: ").split()
nums = [int(x) for x in list3]
    
mn_input = input("Введите множитель (по умолчанию 2): ")
mn = int(mn_input) if mn_input else 2
    
print("Результат (функция):", func(nums, mn))
print("Результат (лямбда-функция):", lambda_func(nums, mn))
