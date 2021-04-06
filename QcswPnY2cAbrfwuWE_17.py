
def filter_factorials(numbers):
    def fact(x):
        if x == 0:
            return 1
        else:
            return x*fact(x-1)
    return [i for i in numbers if i in [fact(j) for j in range(i+1)]]

