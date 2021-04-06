
def boxes(weights):
  arr = []
  rem = 10
  t =  []
  for x in weights:
    if rem - x >= 0:
      rem -= x
      t.append(x)
    else : 
      arr.append(t)
      t = []
      rem = 10
      rem -= x
      t.append(x)
  if len(t) > 0:
    arr.append(t)
  print(arr)
  return len(arr)

