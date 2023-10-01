word = input("Введите слово: ")
n = int(input("Введите номер буквы: "))
if n <= len(word):
    print(word[n - 1])
else:
    print("ОШИБКА")