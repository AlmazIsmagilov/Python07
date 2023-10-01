word1 = str(input("Введите слово 1: "))
word2 = str(input("Введите слово 2: "))
while word1[-1] == word2[0]:
    word = str(input("Введите слово : "))

    if word[-1] == word2[0]:
        word2 = str(input("Введите новое слово : "))

    else:
        print(word)
        break




