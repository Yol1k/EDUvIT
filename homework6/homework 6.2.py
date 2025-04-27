import string

def is_palindrome(text: str) -> bool:
    text = text.lower().replace(" ","")
    text = ''.join(char for char in text if char not in string.punctuation)
    return text == text[::-1]

assert is_palindrome("Лёша на полке клопа нашёл") == True

assert is_palindrome("Лёша на полке, клопа нашёл") == True

assert is_palindrome("12321") == True

assert is_palindrome("Ася, молоко около мяса.") == True

assert is_palindrome("Я с уколов - еле волокуся.") == True
