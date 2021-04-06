
def round_number(num, n):
  low=num-1
  high=num+1
  while low % n !=0:
    low-=1
  while high % n !=0:
    high+=1
  
  return low if num-low < high-num else high

