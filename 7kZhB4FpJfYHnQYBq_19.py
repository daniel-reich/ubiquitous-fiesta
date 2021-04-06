
def lcm_three(num):
  
  a,b,c = num
​
  a = [ a*i for i in range(1,310000) ]
  b = [ b*i for i in range(1,310000) ]
  c = [ c*i for i in range(1,310000) ]
​
  return sorted( list( set(a).intersection(set(b)).intersection(set(c)) ) )[0]

