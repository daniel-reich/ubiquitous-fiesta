
def odd(n):
  n = str(n)
  x = sum(1 for i in n if int(i) % 2)
  return x
​
def even(n):
  n = str(n)
  x = sum(1 for i in n if not int(i) % 2)
  return x
​
def count_digits(lst, key):
​
  if key == 'odd':
    l = [odd(i) for i in lst]
  if key == 'even':
    l = [even(i) for i in lst]
​
  return l

