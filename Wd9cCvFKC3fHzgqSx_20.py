
def num_split(num):
  if num<0:
    return [-x for x in num_split(-num)]
  
  p = 10
  ans = []
  while num:
    x = num % p
    ans.append(x)
    num-=x
    p*=10
​
  return ans[::-1]

