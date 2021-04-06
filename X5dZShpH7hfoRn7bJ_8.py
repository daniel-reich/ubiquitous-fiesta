
def c_fuge(n, k):
  def f(sum,lst):
    if sum in lst:
      return True
    elif sum<=0:
      return False
    else:
      ans=False
      for i in range(len(lst)):
        if f(sum-lst[i],lst)==True:
          ans=True
          break
      return ans
  def lst_prime(x):
    if x==1:
      return []
    elif x==2:
      return [2]
    else:
      first=x
      for i in range(2,int(x**0.5)+1):
        if x%i==0:
          first=i
          break
      return [first]+lst_prime(int(x/first))
  if n==1 or k==1:
    return False
  elif n==k:
    return True
  else:
    if f(k,lst_prime(n))==True and f(n-k,lst_prime(n))==True:
      return True
    else:
      return False

