
def stupid_addition(a, b):
  stri = ""
  num = 0
  if type(a) == type(b) == int:
    stri += str(a)
    stri += str(b)
    print(stri)
    return stri
  if type(a) == type(b) == str:
    num += int(a)
    num += int(b)
    print(num)
    return num
  else:
    return None

