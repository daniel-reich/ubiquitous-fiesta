
def sum_digits(a, b):
 return sum([sum([int(i) for i in list(str(x))]) for x in range(a,b+1)])

