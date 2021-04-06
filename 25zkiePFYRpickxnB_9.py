
def count_boomerangs(lst):
  counter = 0
  for i in range(len(lst)-2):
    print("X")
    if lst[i] == lst[i+2] and lst[i] != lst[i+1]:
      counter += 1
  return counter

