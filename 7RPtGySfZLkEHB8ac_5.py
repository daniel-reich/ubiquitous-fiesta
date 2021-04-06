
from math import floor
def wash_hands(N, nM):
  day = N * 21 #seconds in a day that hands are washed
  month = day * 30
  return str(floor(month*nM/60)) + ' minutes and ' + str(month*nM%60) + ' seconds'

