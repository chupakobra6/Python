for i in range(700001, 701000):
    divs = set()
    for d in range(2, round(i ** 0.5)):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
    if len(divs) > 0:
        m = max(divs) + min(divs)
        if m % 10 == 8:
            print(i, m)