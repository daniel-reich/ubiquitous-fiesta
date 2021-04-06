
import math
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
    
def over_time(lst):
#[0]= start [1] = end [2] = rate [3]= ot_multiplier
#normal time = 9 to 17
  ot = 0
  nt = 0
  if lst[0] > 17  and lst[1]>17:
    pay = (lst[1]-lst[0])*lst[2]*lst[3]
    pay = round_up(pay,2)
    return '$' + str('%.2f' % pay)
  if lst[0]>17:
    ot = lst[0]-17
  if lst[1]>17:
    ot = ot + (lst[1]-17)*lst[3]
  if lst[1]<17:
    nt = lst[1] - lst[0]
  elif lst[0]<17:
    nt = 17- lst[0]
  
  pay =(ot+nt) * lst[2]
  pay = round_up(pay,2)
  
  
  return '$' + str('%.2f' % pay)

