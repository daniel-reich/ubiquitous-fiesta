
def divide(a,b):
  def f(x,y):
    if x < y and x >= 0:
      return 0
    return f(x-y,y)+1 
  if a <= 0 and b <= 0:
    return f(abs(a),abs(b))
  elif a < 0 and b >= 0:
    return f(abs(a),b)*-1
  elif a >= 0 and b < 0:
    return f(a,abs(b))*-1
  return f(a,b)

