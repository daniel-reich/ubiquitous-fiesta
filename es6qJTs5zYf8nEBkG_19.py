
def is_rectangle(coordinates):
  if len(coordinates) != 4:
    return False
  c = [tuple_convert(i) for i in coordinates]
  c.sort()
  if c[0][0]==c[1][0] and c[1][1]==c[3][1] and c[3][0]==c[2][0] and c[2][1]==c[0][1]:
    return True
  return False
​
def tuple_convert(str):
  str = str.replace(" ","")
  n = str.index(",")
  return (int(str[1:n]),int(str[n+1:-1]))

