
def filter_factorials(n):
  def is_fact(x):
    i=1
    while(True):
      if x%i<1:x//=i
      else:break
      i+=1
    return x==1
  return[i for i in n if is_fact(i)]

