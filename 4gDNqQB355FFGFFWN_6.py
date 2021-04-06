
def available_spots(lst, num):
  counter = 0
  for x,y in zip(lst,lst[1::]):
    if num%2 == 0:
      if (x%2 == 0 and y%2 == 0) or (x%2 != 0 and y%2 == 0) or (x%2 == 0 and y%2 != 0):
        counter += 1
    else:
      if (x%2 != 0 and y%2 != 0) or (x%2 != 0 and y%2 == 0) or (x%2 == 0 and y%2 != 0):
        counter += 1
  return counter

