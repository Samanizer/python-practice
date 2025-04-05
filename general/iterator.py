s = "abc"
t = "axhftbksh"

it = iter(t)

print([c in it for c in s])

print(id(t))