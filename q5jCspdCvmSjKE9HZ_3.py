
def lcm_of_list(numbers):
  l = lcm(numbers[0],numbers[1])
  for i in numbers:
    l = lcm(l,i)
  return l
​
def lcm(x,y):
  return (x*y)//gcf(x,y)
​
def gcf(a,b):
  if b == 0:
    return a
  return gcf(b,a%b)

