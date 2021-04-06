
def sum_digits(a, b):
  return sum([sum(list(map(int,list(str(n))))) for n in range(a,b+1)])

