
def lychrel(n):
  current = n
  if str(n) == str(n)[::-1]:
    return 0
  a = 1
  while a <= 500:
    back = int(str(current)[::-1])
    sum = current + back
    if str(sum) == str(sum)[::-1]:
      return a
    current = sum
    a += 1
  return True

