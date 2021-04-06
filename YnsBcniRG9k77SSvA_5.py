
def print_all_groups():
  arr=[]
  for x in ["1","2","3","4","5","6"]:
    for y in ["a","b","c","d","e"]:
      arr.append(x+y)
  return ', '.join(arr)

