a = input("Первый текст:")
b = input("Второй текст:")
c = []
for i in a.split(" "):
    if i in b.split(" "):
        c.append(i)
print(c)