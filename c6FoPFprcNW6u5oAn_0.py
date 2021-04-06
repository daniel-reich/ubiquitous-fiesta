
def farey(n):
  def cf(x,y):
    return [i for i in range(2,min(x,y)+1) if not (x%i or y%i)]
    
  return ["0/1"] + \
  sorted(["{}/{}".format(x,y) for x in range(1,n) for y in range(1,n+1) if x<y and not cf(x,y)],key=eval) \
  + ["1/1"]

