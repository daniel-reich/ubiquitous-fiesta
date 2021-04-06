
def describe_num(n):
  res = "The most brilliant"
  if n % 2 == 0:
    res += " exciting"
  if n % 3 == 0:
    res += " fantastic"
  if n % 4 == 0:
    res += " virtuous"
  if n % 5 == 0:
    res += " heart-warming"
  if n % 6 == 0:
    res += " tear-jerking"
  if n % 7 == 0:
    res += " beautiful"
  if n % 8 == 0:
    res += " exhilarating"
  if n % 9 == 0:
    res += " emotional"
  if n % 10 == 0:
    res += " inspiring"
  res += " number is " + str(n) + "!"
  return res

