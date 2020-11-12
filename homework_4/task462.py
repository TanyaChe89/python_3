from itertools import cycle

c = 0
for el in cycle([10, 20, 30]):
    if c > 5:
        break
    print(el)
    c += 1