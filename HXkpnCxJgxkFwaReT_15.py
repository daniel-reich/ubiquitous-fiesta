
def count_datatypes(*args):
  types = [0,0,0,0,0,0]
​
  for i in args: 
    if type(i) == int:
      types[0] += 1
    elif type(i) == str:
      types[1] += 1
    elif type(i) == bool:
      types[2] += 1
    elif type(i) == list:
      types[3] += 1
    elif type(i) == tuple:
      types[4] += 1
    else:
      types[5] += 1
    
  return types

