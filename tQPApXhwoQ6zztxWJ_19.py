
def get_prices(lst):
  b = []
  
  for i in lst:
    a = i.split(' ')
    b.append(a)
  
  d = []
  for i in b:
    c = i[len(i)-1][2:len(i[len(i)-1])-1]
    d.append(float(c))
    
  return d

