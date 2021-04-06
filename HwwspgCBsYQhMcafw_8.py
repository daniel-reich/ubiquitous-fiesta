
def digit_sum(n):
  return sum(int(x) for x in str(n))
def super_digit(n, k):
  s=int(n*k)
  while len(str(s))>1:
    s=digit_sum(s)
  return s

