import random
n = int(input("Введите n:"))
a = []
for i in range(n):
    a.append(random.randint(-100, 100))
print(a)
