
def get_drink_ID(fl, ml):
  a=fl.split()
  b=list(map(lambda x:x[0:3], a))
  b=[i.upper() for i in b]
  return "".join(b)+ml.replace("ml",'')

