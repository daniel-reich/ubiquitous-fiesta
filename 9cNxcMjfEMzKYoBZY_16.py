
def num_type(n):
  d = lambda n:sum([i for i in range(1,n) if not n%i])
  return "Perfect" if d(n)==n else "Amicable" if d(d(n))==n else "Neither"

