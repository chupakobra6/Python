with open('26.txt') as f:
    data = f.readlines()
    s, n = map(int, data[0].split())
    del data[0]
    data = sorted(map(int, data))
    answer = []
    for i in data:
        if sum(answer) + i > s: break
        answer.append(i)
    print(sum(answer), data.index(i))
    list = [x for x in data if x - i <= s - sum(answer)]
    print(max(list))