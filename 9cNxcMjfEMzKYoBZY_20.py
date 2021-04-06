
def divisors(n):
  return [i for i in range(1,n) if n%i == 0]
​
def num_type(n):
  if sum(divisors(n)) == n:
    return 'Perfect'
  if sum(divisors(sum(divisors(n)))) == n:
    return 'Amicable'
  return 'Neither'

