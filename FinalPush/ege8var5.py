s = 'пир'
count = 0

for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e 
                    if word.count('п') == 1:
                        count += 1
                        
print(count)