
def func(num):
    return sum(int(c) for c in str(num)) - pow(len(str(num)), 2)

