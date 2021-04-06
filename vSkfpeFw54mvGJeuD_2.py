
def lychrel(n):
  if str(n) == str(n)[::-1]:
    return 0
  count = 0
  for i in range(500):
    n += int(str(n)[::-1])
    count += 1
    if str(n) == str(n)[::-1]:
      return count
  return True

