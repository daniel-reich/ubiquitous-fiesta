
def available_spots(lst, num):
  if num&1:
    return len(lst)-1 - sum(not lst[i]&1 and not lst[i+1]&1 for i in range(len(lst)-1))
  else:
    return len(lst)-1 - sum(lst[i]&1 and lst[i+1]&1 for i in range(len(lst)-1))

