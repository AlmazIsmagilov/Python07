step = int(input("Введите шаг: "))
word = input("Введите предложение: ")
for i in word:
   new_word = ord(i) + step
   if ord(i) < 1040 or ord(i) > 1103:
       print(i, end="")
   elif 1072 <= ord(i) <= 1103:
       if new_word > 1103:
           print(chr(1072 + (new_word - 1104)), end="")
       else:
           print(chr(new_word), end="")
   else:
       if new_word > 1071:
           print(chr(1040 + (new_word - 1072)), end="")
       else:
           print(chr(new_word), end="")
