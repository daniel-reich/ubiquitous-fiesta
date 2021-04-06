
import math
def car_timer(n):
  if len(str(n))==3:return math.ceil(n/60)
  if len(str(n))==4:return int((str(n)[0])+(str(n)[-1]))
  return sum([int(i) for i in ' '.join(x for x in str(n).replace(',','')).split(' ')])

