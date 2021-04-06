
def divisible_by_b(a, b):
    c = a+1 
    o = c%b
    if o == 0:
        return c
    else:
        for i in range(a, a*1000):
            p = i%b
            if p == 0:
                print("yes")
                return i

