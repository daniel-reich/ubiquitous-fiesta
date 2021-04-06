
def multiply(x):
    def compute(a):
        return [a * y for y in x]
    return compute

