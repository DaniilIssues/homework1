a = [2, -5, 8, 9, -25, 25, 4]
b = []
import math
for i in a:
    if i <= 0:
        continue
    if math.sqrt(i) == int(math.sqrt(i)):
        b.append(int(math.sqrt(i)))
print(b)
