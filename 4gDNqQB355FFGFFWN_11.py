
def available_spots(lst, n):
  if not n%2: return sum(1 for x,y in zip(lst,lst[1:]) if not x%2 or not y%2)
  return sum(1 for x,y in zip(lst,lst[1:]) if x%2 or y%2)

