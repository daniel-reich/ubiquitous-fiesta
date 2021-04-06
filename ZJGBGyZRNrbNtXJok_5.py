
def nearest_vowel(s):
  x=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  a=s
  y=[]
  o=['a','e','i','o','u']
  d={}
  v=[]
  count=24
  for i in range(len(x)):
    if x[i]==a:
      e=i
      y.append(abs((e+1)-1))
      y.append(abs((e+1)-5))
      y.append(abs((e+1)-9))
      y.append(abs((e+1)-15))
      y.append(abs((e+1)-21))
  for i in range(len(y)):
    d[o[i]]=y[i]
  for i in d.keys():
    if min(d.values())==d.get(i):
      v.append(i)
  return(min(v))

