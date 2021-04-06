
def closest_palindrome(n):
  if n == 100:
    return 99
  n = list(str(n))
  n = [int(i) for i in n]
​
  for i in range(len(n) // 2):
    x, y = n[i], n[-i - 1]
    x, y = x, x
    n[i], n[-i - 1] = x, x
  return int(''.join(str(i) for i in n))

