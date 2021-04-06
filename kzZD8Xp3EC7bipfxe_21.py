
def worded_math(equ):
  z = ''
  lst = [('zero','0'),('one','1'),('two','2'),('minus','-'),('plus','+')]
  for i in equ.split():
    for x,y in lst:
      if i.lower() == x:
        z += y
  z = eval(z)
  for x,y in lst:
    if y == str(z):
      return x.capitalize()

