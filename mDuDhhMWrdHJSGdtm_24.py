
def divisors(n):
  yield 1
  yield n
  i = 2
  while i < n//i:
    if not n%i:
      yield i
      yield n//i
    i+=1
  if i**2==n: yield i
​
def is_exactly_three(n):
  return len(list(divisors(n)))==3

