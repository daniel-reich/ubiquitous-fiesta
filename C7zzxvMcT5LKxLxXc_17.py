
def sum_str(a):
  return sum([int(i) for i in str(a)])
​
def decode(txt):
  return [sum_str(j) for j in [ord(i) for i in txt]]

