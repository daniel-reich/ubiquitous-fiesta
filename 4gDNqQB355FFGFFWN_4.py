
def available_spots(lst, num):
  return sum(l%2|r%2 if num%2 else not (l%2&r%2) for l,r in zip(lst, lst[1:]))

