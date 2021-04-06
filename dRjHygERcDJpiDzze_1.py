
def lengthen(s1, s2):
  s1, s2 = min(s1,s2,key=len),max(s1,s2,key=len)
  val1 = len(s2)//len(s1)
  val2 = len(s2)%len(s1)
​
  return s1*val1 + s1[:val2]

