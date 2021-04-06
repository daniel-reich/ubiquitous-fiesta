
def simplify(txt):
  n,d = int(txt.split("/")[0]),int(txt.split("/")[1])
  g = gcd(n,d)
  if gcd==1:  return txt
  else:
    n /= g
    d /= g
  return str(int(n))+"/"+str(int(d)) if int(d)!=1 else str(int(n))
  
def gcd(a,b):
  if(b==0): return a
  else: return gcd(b,a%b)

