
def lychrel(n):
  if str(n) == str(n)[::-1]:
    return 0
  else:
    counter = 0
    while str(n) != str(n)[::-1]:
      n = n + int(str(n)[::-1])
      counter += 1
      if counter >= 500:
        return True
  return (counter)

