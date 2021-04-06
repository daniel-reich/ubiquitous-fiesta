
def maxmin(n):
  def f(n,l):
    for i,x in enumerate(l):
      if x!=n[i]:p=i+n[i:].rfind(x);return int(n[:i]+n[p]+n[i+1:p]+n[i]+n[p+1:])
    return int(n)
  n=str(n)
  return f(n,sorted(n,reverse=1)),f(n,[min(n,key=lambda y:(y,'z')[y=='0'])]+sorted(n[1:]))

