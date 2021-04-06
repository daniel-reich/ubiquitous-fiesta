
def describe_num(n):
  s = "The most brilliant"
  if not n % 2:
    s += " exciting"
  if not n % 3:
    s += " fantastic"
  if not n % 4:
    s +=  " virtuous"
  if not n % 5:
    s +=  " heart-warming"
  if not n % 6:
    s +=  " tear-jerking"
  if not n % 7:
    s +=  " beautiful"
  if not n % 8:
    s +=  " exhilarating"
  if not n % 9:
    s +=  " emotional"
  if not n % 10:
    s +=  " inspiring"
  return "{} number is {}!".format(s, n)

