
def blocks(step):
  if step==0:
    return 0
  elif step==1:
    return 5
  else:
    return ((step-1)*(6)+((step*(step-1))/2)+5)

