
def odd(num):
  return abs(num)//2-abs(num)/2
def bitwise_index(lst):
  max=None
  index=-1
  for i,num in enumerate(lst):
    if not odd(num) and (max==None or num>max):
      max=num
      index=i
  if max==None:
    return "No even integer found!"
  if not odd(index):
    return {"@even index " + str(index): max}
  else:
    return {"@odd index " + str(index): max}

