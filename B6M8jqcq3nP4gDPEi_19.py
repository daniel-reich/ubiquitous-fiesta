
def iso_group(lst):
  # your recursive solution here
  if lst[0] != "potato":
    lst = ["potato", lst[0] - 1, 0, 0] + lst
  else:
    i = lst[2] + 4
    if i < len(lst):    
      if lst[i] > lst[1]:
        lst[3] = 1
        lst[1] = lst[i]
      elif lst[i] == lst[1]:
        lst[3] += 1
      lst[2] += 1
    else:
      if lst[3] == 1:
        return lst[1]
      else:
        return [lst[1]]*lst[3]
  return iso_group(lst)

