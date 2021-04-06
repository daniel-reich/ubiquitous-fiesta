
import re
def count_eatable_chocolates(total_money, cost_of_one_chocolate):
  m = int(re.findall(r'\d+', total_money)[0])
  c = int(re.findall(r'-?\d+', cost_of_one_chocolate)[0])
  if c<1: return 'Invalid Input'
  ans = m//c
  w = m//c
  while w>2:
    new = w//3
    ans+=new
    w-= 2*new
  return ans

