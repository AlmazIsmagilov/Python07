step = int(input("Введите шаг: "))
word = input("Введите предложение: ")

for i in word:
    if ord(i) >= 1101:
        i = chr(ord(i) - 29)
    else:
        i = chr(ord(i) + step)

    print(i, end="")
