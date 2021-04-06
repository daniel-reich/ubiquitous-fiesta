
def num_type(n):
  div_sum = lambda n: sum(i for i in range(1,n) if n%i == 0)
  if div_sum(n) == n: return "Perfect"
  if div_sum(div_sum(n)) == n: return "Amicable"
  return "Neither"

