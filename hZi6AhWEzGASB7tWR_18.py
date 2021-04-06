
def check(lst):
  increase = True;
  decrease = True;
  
  for i in range(len(lst)-1):
    if lst[i+1] >= lst[i]:
      decrease = False;
    if lst[i+1] <= lst[i]:
      increase = False;
      
  print("Decrease: " + str(decrease))
  print("Increase: " + str(increase))
  
  if increase == True:
    return "increasing"
  if decrease == True:
    return "decreasing"
  else:
    return "neither"

