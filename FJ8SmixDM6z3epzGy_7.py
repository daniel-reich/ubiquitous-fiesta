
def check_perfect(x):
    return sum([i for i in range(1,x) if x%i == 0]) == x

