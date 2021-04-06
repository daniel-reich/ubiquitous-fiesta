
def has_consecutive_series(lst1, lst2):
  if len(lst1)<len(lst2):return has_consecutive_series(lst2, lst1)
  if len(lst1)>len(lst2):return has_consecutive_series(lst1, lst2 + [0]* (len(lst1)-len(lst2)) )
  s=sum(lst1)+sum(lst2)
  n=max(len(lst1),len(lst2)) # both list have same length
  t=s- (n)*(n-1)//2 # sum(lists) - sum(0..n-1)
  if t%n !=0: return False
  t=t//n # starting value; sum(lists)= sum(t,t+1, ... , t+n-1)
​
  print(s,n,t)
  
  def test(lst1,lst2,t):
    if len(lst1)==0: return True
    for idx,x in enumerate(lst1):
      if (t-x) in lst2:
        tmp=lst2.index(t-x)
        if test(lst1[:idx]+lst1[idx+1:], lst2[:tmp]+lst2[tmp+1:],t+1):
          return True
    return False
  
  return test(lst1,lst2,t)

