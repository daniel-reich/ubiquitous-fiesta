
def num_in_str(lst):
  new = []
  for str in lst:
    for char in str:
      if char.isdigit() and str not in new:
        new.append(str)
  return(new)

