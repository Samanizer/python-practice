l = [(20,1), (10, 2), (30, 1), (30, 2)]

l.sort(key=lambda x: (x[0], x[1]))

print(l)