a = [x / 10 for x in range(0, 11, 1)]
print(a)

b = set((x, x ** 2, x ** 3) for x in range(-10, 11))
print(b)

napisy = ['kot', 'pies', 'żaba', 'skowronek', 'nutria']

c = {x: len(x) for x in napisy}
print(c)
