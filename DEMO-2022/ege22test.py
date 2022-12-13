for x in range (1, 100):
    q = 9
    l = 0
    x1 = x
    while x1 >= q:
        l = l + 1
        x1 = x1 - q
    m = x1
    if m < l:
        m = l
        l = x1
    if l == 4 and m == 5:
        print(x)
