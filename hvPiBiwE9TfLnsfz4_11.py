
def generate_word(n):
  if n<2: return "invalid"
  
  def gw(n):
    if n==1:return "b"
    if n==2:return "a"
    return gw(n-2)+gw(n-1)
​
  return ', '.join([gw(i) for i in range(1,n+1)])

