
def smallest(length, number):
    for i in range(10**(length-1), 10*10**length, 1):
        if i % number == 0:
            if len(list(str(i))) >= length:
                return i

