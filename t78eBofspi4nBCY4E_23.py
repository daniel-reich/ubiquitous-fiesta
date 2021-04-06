
base=list("abcdefghijklmnopqrstuvwxyz")
​
def base_conv(n, b):
  if type(n)==int:
    out=[]
    while n>0:
      out.append(base[n%b])
      n=(n-n%b)//b
    return ''.join(out[::-1])
​
  if ord(max(list(n)))-ord('a')>=b or min(list(n))<'a': return n+" is not a base "+str(b)+" number."
  return sum([(ord(x)-ord('a'))*(b**idx) for idx,x in enumerate(n[::-1])])

