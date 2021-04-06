
def box_seq(step):
  if step==0:
    return 0 
  elif step == 1 : 
    return 3
  elif step == 2 :
    return 2
  elif step%2==1:
    return step + 2
  elif step%2==0:
    return step

