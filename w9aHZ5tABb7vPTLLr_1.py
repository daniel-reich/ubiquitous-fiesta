
def lucky_ticket(n_digits):
  gen = [1 for i in range(10)]
  power = [1]
  for i in range(n_digits):
    power = poly_mult(power,gen)
  return power[9*n_digits//2]
​
​
def poly_mult(c1, c2):
    n, m = len(c1), len(c2)
    prod = []
    for k in range(n+m-1):
        prod.append(sum(c1[i]*c2[k-i] for i in range(max(0, k-m+1), min(n, k+1))))
    return prod

