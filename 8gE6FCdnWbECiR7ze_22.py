
def smith_type(number):
  def ip(n):
    return n==2 or all(n%d for d in range(3,int(n**.5)+1,2)) and bool(n%2) and n>2
  
  def pf(num):
    output = []
    for i in range(2, num//2+1):
      while not num % i:
        output.append(i)
        num //= i
    return output
​
  def dr(num):
    while num > 9:
      num = sum(int(x) for x in str(num))
    return num
​
  def sm(num):
    return dr(num)==dr(sum(pf(num)))
    
  if ip(number):
    return "Trivial Smith"
  elif sm(number):
    if sm(number-1):
      return "Oldest Smith"
    elif sm(number+1):
      return "Youngest Smith"
    else:
      return "Single Smith"
  else:
    return "Not a Smith"

