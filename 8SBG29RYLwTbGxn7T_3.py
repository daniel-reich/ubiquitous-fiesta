
def free_shipping(order):
  sum=0
  for s in order.values():
    sum=sum+s
  if(sum>50):
    return True
  else:
    return False

