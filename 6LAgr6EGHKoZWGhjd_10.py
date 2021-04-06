
def final_direction(initial, turns):
  lst = ["N", "E", "S", "W"]
  count = lst.index(initial)
  for i in turns:
    if i == "R":
      count += 1
    if i == "L":
      count -= 1
    if count == 4:
      count = 0
    if count == -1:
      count = 3
  return lst[count]

