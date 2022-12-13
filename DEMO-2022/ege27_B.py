with open('C:/Python/DEMO-2022/27_B.txt') as f:
    n = int(f.readline())
    min_sum = 43 * [100000000000000]
    min_len = 43 * [0]
    summa, maxsum, minLength, ms, ln = 0, 0, 0, 0, 0
    for i in range(n):
        summa += int(f.readline())
        d = summa % 43
        if d == 0:
            maxsum = summa
            minLenght = i
        else:
            ms = summa - min_sum[d]
            ln = i - min_len[d]
            if ms > maxsum or (ms == maxsum and ln < minLenght):
                maxsum = ms
                minLenght = ln
        if summa < min_sum[d]:
            min_sum[d] = summa
            min_len[d] = i
    print(minLenght)
