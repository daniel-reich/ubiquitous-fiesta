
def divisible_by_b(a, b):
  c = list(range(a,a + b + 1))
  d = [i for i in c if i % b == 0]
  return min(d)

