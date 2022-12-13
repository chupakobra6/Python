for A in range(150):
    f = 1
    for x in range(300):
        if ((x & 29 != 0) <= ((x & 12 == 0) <= (x & A != 0))) == 0:
            f = 0
    if f == 1:
        print(A)

for A in range(150):
    f = 1
    for x in range(1, 300):
        for y in range(1, 300):
            if ((-2 * y + x < A) or (x > 8) or (y > 100)) == 0:
                f = 0

    if f == 1:
        print(A)