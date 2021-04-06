
def mystery_func(num):
​
    import math
​
    dos = int(math.sqrt(num))*'2'
​
    return int(dos+str(num-2**len(dos)))

