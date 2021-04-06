
def safecracker(start, increments):
  n1 = start - increments[0]
  n2 = n1 + increments[1]
  n3 = n2 - increments[2]
  lst = [n1, n2, n3]
  return [x-100 if x>100 else x+100 if x<0 else x for x in lst]

