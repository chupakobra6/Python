c = 0
for x in range(100, 1000):
    n = int(str(x)[:1]) + int(str(x)[1:2])
    s = int(str(x)[1:2]) + int(str(x)[2:3])
    k = str(n) + str(s)
    if k == '1216':
        c += 1
    j = str(s) + str(n)
    if j == '1216':
        c += 1
    
print(c)