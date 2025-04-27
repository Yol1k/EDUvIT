def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)

assert average_num([1, 1, 1]) == 1
assert average_num([1.5,2.5, 3.5]) == 2.5
assert average_num(['1', '2', '3']) == 2
assert average_num(['a', 'b', 'c']) == "Bad request"
assert average_num(['a']) == "Bad request"
assert average_num(['']) == "Bad request"
assert average_num(['1', '2', 3]) == 2
assert average_num(['1', '2', 3, 4]) == 2.5
assert average_num([-1, -1, -1]) == -1
assert average_num([-1]) == -1
assert average_num([1.488, 1.488]) == 1.49
assert average_num([1.555, 1.555]) == 1.55

