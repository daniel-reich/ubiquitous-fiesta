
def available_spots(lst, num):
  if num%2:
    return sum(1 for i in range(len(lst)-1) if (lst[i]%2 or lst[i+1]%2))
  else:
    return sum(1 for i in range(len(lst)-1) if not(lst[i]%2 and lst[i+1]%2))

