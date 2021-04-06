
def cutting_grass(lst, *cuts):
  lawn = lst
  ret = []
  print(lst)
  for cut in cuts:
    for i in range(len(lawn)):
      lawn[i] -= cut
    
    if len([x for x in lawn if x <= 0]) == 0:
      ret.append(lawn.copy())
    else:
      ret.append("Done")
      
  return ret

