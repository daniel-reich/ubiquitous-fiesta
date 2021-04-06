
'''
import math
def trailing_zeros(n):
  fact = math.factorial(n)
  as_str = str(fact)[::-1]
  i = 0
  while True:
    if(as_str[i]!="0"):
      break
    i+=1
  return i
'''
def trailing_zeros(n):
  current_power_of_5 = 5
  zeros = 0
  while(True):
    div = n//current_power_of_5
    zeros+=div
    if(div==0):
      break
    current_power_of_5*=5
  return zeros

