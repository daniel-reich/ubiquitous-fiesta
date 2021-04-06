
def untuple(ins):
  sum = 0
  for x in ins:
    sum += check_type(x)
  return round(float(sum), 1)
  
def unlist(ins):
  sum = 0
  for x in ins:
    sum += 1/check_type(x)
  return round(1/sum, 1)
  
def check_type(ins):
  if type(ins) == int:
    return ins
  elif type(ins) == tuple:
    return untuple(ins)
  elif type(ins) == list:
    return unlist(ins)
    
def resist(net):
  return check_type(eval(net))

