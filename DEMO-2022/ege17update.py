with open('17.txt') as f:
    s =[int(x) for x in f]
    numbers = []
    maximum = -10001
    for j in s:
        if j % 3 == 0 and j > maximum:
            maximum = j
    for i in range(1, len(s)):
        if (s[i] % 3 == 0 or s[i - 1] % 3 == 0) and (s[i] + s[i - 1]) <= maximum:
            numbers.append(s[i] + s[i - 1])
print(len(numbers), max(numbers), maximum)