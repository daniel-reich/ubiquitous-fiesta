
def perimeter(lst):
  a,b,c = lst
  return round(leng(a,b)+leng(a,c)+leng(b,c),2)
  
​
def leng(a,b):
  return ((a[0]-b[0])**2+(a[1]-b[1])**2)**.5

