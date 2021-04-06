
def mystery_func(num):
    intlog = 1
    while 2**(intlog+1) < num: intlog += 1
    return int('2'*(intlog))*10 + num-2**(intlog)

