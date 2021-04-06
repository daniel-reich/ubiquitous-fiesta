
def million_in_month(first_month, multiplier):
    #goal = 10**6# or 1000000;
    savings=0
    
    count=0
    
    while savings<=10**6:
      savings+=first_month
      first_month*=multiplier
      count+=1
    return count

