
def range_of_num(start, end):
  if type(start) != int or type(end) != int:
    raise TypeError("Invalid arg to range_of_num")
  returner = []
  start += 1
  while(start < end):
      returner.append(start)
      start+=1
  return returner

