m = []

for x in range(100, 3000):
    n = bin(x)[2:]
    s = int(n[1:])
    r = int(n) - int(s)
    m.append(r)

print(len(set(m)))