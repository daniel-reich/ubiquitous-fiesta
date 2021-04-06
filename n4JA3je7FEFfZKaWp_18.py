
def million_in_month(first_month, multiplier):
    #goal = 10**6# or 1000000;
  i=0
  s=0
  while s<1000000:
    s+=first_month*(multiplier)**i
    i+=1
  return i

