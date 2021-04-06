
def parallel_resistance(lst):
    a = 0
    for i in lst:
        a += 1/i
    
    a = round(1/a,1)
    return a

