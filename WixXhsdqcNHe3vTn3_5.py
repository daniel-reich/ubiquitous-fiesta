
def is_prime(n):
  for i in range(2,int(n**0.5)+1):
    if n % i == 0:
      return False
  return False if n == 1 else True
​
def how_bad(n):
  ones = bin(n).count('1')
  res = ["Odious"] if ones % 2 == 1 else ["Evil"]
  return res + ["Pernicious"] if is_prime(ones) else res

