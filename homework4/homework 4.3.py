def func(text, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write('\n' + text)

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i in lines[1::2]:
            print(i.strip())
func("Добавленная строка", "text1.txt")
