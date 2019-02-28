a = [1, 2, 3, 4, 4, 4, 4, 5, 9, "rep", "qwwar"]
b = [1, 5, 4, 6, "qwwar"]
for i in b:
    for x in b:
        if x in a:
            a.remove(x)
print(a)
