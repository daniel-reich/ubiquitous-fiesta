
def maxmin(n):
  s=str(n)
  maxx,minn, lst=n,n,[]
  for i in range (len(s)):
    for j in range(1,len(s)):
      out=list(s)
      out[j],out[i]=s[i],s[j]
      lst.append(int(''.join(out)))
  lst1 = [i for i in lst if i > 10**(len(s)-1)]
  return (max(lst1),min(lst1))

