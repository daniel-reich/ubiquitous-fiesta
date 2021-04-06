
def prime(n):
  return sum([1 for i in range(1, n + 1) if n % i == 0]) == 2
​
​
def prime_in_range(n1, n2):
  return any([prime(i) for i in range(n1, n2 + 1)])

