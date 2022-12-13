with open('C:/Python/FinalPush/17.txt') as f:
    num = [int(x) for x in f]
    s = []

    for i in range(len(num) - 1):
        for j in range(i + 1, len(num)):
            if (num[i] + num[j]) % 120 == 0:
                s.append(num[i] + num[j])
        
print(len(s), max(s))
