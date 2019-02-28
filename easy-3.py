a = [5, 5, 7, 8, 90, 123, 556, 5]
b = []
for i in a:
    if i % 2 == 0:
        b.append(i/4)
    else:
        b.append(i*2)
print(b)
