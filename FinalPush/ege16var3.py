def F(n):
    if n <= 3:
        return n + 3
    else:
        if F(n - 1) % 2 == 0:
            return F(n - 2) + n
        else:
            return F(n - 2) + 2 * n

s = 0
for i in range(40, 51):
    s += F(i)
print(s)

# don't work