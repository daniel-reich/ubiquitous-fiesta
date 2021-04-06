
def num_in_str(lst):
  new=[]
  for x in lst:
    for y in x:
      if y.isdigit():
        new.append(x)
        break
  return new

