
def reverse_case(txt):
  x = ""
  for char in txt:
    if char.islower() :
      x= x+char.upper()
    else:
      x =x+char.lower()
  return x

