def function_name(search: str, status: bool, *args: int | str, **kwargs: str):
    """
    Функция function_name обрабатывает аргументы в зависимости от параметров search и status.

    Аргументы:
        search: Обрабатывает "args" или "kwargs".
        status: Если True, добавляет числа из args в список и возвращает этот список, если False, то возвращает строку из args.
        *args: Позиционные аргументы (целые числа или строки).
        **kwargs: Именованные аргументы (строки).

    Возвращает:
        - При search="args" и status=True: список целых чисел из args.
        - При search="args" и status=False: строку с объединением args.
        - При search="kwargs": строку в формате "Key: k, Value: v;".

    Ошибка:
        ValueError: Если search не "args" или не "kwargs".
    """
    result: List[int] = []
    result_2: str = ""
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")
