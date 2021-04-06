
def lychrel(n):
  counter = 0
  while counter < 500:
    if str(n) == str(n)[::-1]:
      return counter
    counter += 1
    n = n + int(str(n)[::-1])
  return True

