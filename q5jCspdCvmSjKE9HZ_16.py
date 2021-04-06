
def lcm_of_list(numbers):
  n = 1
  for i in numbers:
    n = (n*i)//gcd(n,i)
  return n
​
def gcd(a,b): 
  if(b==0): 
    return a 
  else: 
    return gcd(b,a%b)

