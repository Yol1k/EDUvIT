def gen_func():
    for x in range(2,10**6):
        count = 0
        for y in range(2, int(x**0.5) + 1):
            if x % y == 0 and x != y:
                count+=1
                if count > 0:
                    break
        if count == 0:
            yield x
            
gen = gen_func()
for i in range(100):
    print(next(gen))
