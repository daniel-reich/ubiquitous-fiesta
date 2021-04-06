
def bemirp(n):
  def ip(x):
    return x==2 or all(x%d for d in range(3,int(x**.5)+1,2)) and x%2 and x>2
​
  ud = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
  if ip(n):
    if ip(int(str(n)[::-1])) and str(n)!=str(n)[::-1]:
      if {int(y) for y in str(n)} <= {0,1,6,8,9} and ip(int("".join(ud.get(z) for z in str(n)))):
        return "B"
      return "E"
    return "P"
  return "C"

