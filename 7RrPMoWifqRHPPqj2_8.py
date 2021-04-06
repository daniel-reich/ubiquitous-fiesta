
def safecracker(start, increments):
  lst = [0, 0, 0]
  lst[0] += start - increments[0]
  lst[1] += lst[0] + increments[1]
  lst[2] += lst[1] - increments[2]
  
  return [i+100 if i < 0 else i-100 if i > 100 else i for i in lst]

