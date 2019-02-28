text = input("Введите текст:")
stat1 = {}
stat2 = 0
dictionary = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in text.split(" "):
    if i not in stat1:
        stat1[i] = 1
    else:
        stat1[i] += 1
for i in text:
    if i in dictionary:
        stat2 += 1
print(stat1)
print(stat2, "английских букв в тексте")
