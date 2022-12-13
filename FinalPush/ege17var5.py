with open('C:/Python/FinalPush/17 (2).txt') as f:
    num = [int(x) for x in f]
    s = []

    for i in range(1, len(num)):
        if num[i] % 3 == 0 or num[i - 1] % 3 == 0:
            s.append(num[i] + num[i - 1])

print(len(s), max(s))