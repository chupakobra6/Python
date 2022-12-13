print('P Q R')
for p in range(2):
    for q in range(2):
        for r in range(2):
            if (not p and q) is r:
                print(p, q, r)