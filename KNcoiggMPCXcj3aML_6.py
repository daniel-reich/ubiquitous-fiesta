
def number_of_days(coordinate):
  import math
  l=sum(map(abs,coordinate))
  
  return l+math.ceil(l/5)-1

