def F(n):
    if n == 0:
        return 0
    if n > 0:
        if n % 2 == 0:
            return F(n/2) + 3
        else:
            return 2 * F(n - 1) + 1

m = set()

for i in range(1, 1001):
    m.add(F(i))

print(len(m))