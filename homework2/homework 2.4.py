#Задание 4. Подсчет количества слов
text = input("Введите строку: ").split()
words = set(text)

for word in words:
    count = text.count(word)
    print(f"{word}: {count}")
