
def seesaw(num):
  txt = str(num or 0)
  le, ri = txt[:len(txt)//2], txt[-(-len(txt)//2):]
  return 'left' if le > ri else 'right' if ri > le else 'balanced'

