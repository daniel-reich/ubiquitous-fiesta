
def available_spots(lst, num):
  k=sum([(lst[i]%2 or lst[i+1]%2) for i in range(len(lst)-1)])
  l=sum([(lst[i]%2 and lst[i+1]%2) for i in range(len(lst)-1)])
  return k if num%2 else len(lst)-l-1

