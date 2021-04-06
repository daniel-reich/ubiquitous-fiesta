
def expanded_form(num, x = "+"):
  for i in range(len(str(num))):
    a = num % (10**(i+1))
    if a:
      x += str(a)[::-1] + " + "
      num -= a
  return x[-4:0:-1]

