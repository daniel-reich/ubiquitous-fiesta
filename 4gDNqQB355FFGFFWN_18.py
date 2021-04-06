
def available_spots(lst, num):
  sum1=0
  for i in range(len(lst[:-1])):
    if num%2==0:
      if lst[i]%2!=0 and lst[i+1]%2!=0 :
        sum1+=0
      else:
        sum1+=1
    if num%2!=0:
      if lst[i]%2==0 and lst[i+1]%2==0 :
        sum1+=0
      else:
        sum1+=1
  return sum1

