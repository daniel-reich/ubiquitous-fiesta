
def total_volume(*boxes):
  arr = []
  for x in boxes:
    prod = 1
    for y in x:
      prod *=y 
    arr.append(prod)
  return sum(arr)

