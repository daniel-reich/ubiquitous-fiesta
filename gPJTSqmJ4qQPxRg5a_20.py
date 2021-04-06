
def func(num):
    return sum([int(i)-len(str(num)) for i in str(num)])

