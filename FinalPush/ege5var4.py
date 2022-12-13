c = 0
for x in range(1001, 10000, 2):
    n = int(str(x)[:1]) + int(str(x)[1:2])
    s = int(str(x)[2:3]) + int(str(x)[3:4])
    k = str(n) + str(s)
    if k == '414':
        c += 1

print(c)