
def find_digits(m):
    digits = []
    while abs(m) > 9:
        digits.append(m % 10)
        m //= 10
    else:
        digits.append(m)
​
    return len(set(digits)) == 2
​
def doubleton(n):
  n += 1
  while not find_digits(n):
    n += 1
  return n

