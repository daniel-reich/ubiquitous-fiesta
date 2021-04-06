
def flip_list(lst):
  flipped = []
​
  for item in lst:
    if (isinstance(item, list)):
      flipped.append(item[0])
​
    else:
      flipped.append([item])
​
  return flipped

