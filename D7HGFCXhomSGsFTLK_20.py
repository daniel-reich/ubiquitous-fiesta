
def convert_cartesian(x, y):
  coords = zip(x,y)
  ans_coords = []
  for pair in coords:
    lst = [pair[0],pair[1]]
    ans_coords.append(lst)
    
  return ans_coords

