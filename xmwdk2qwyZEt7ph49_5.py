
def get_length(l):
​
  c = 0
​
  for i in l: 
​
    if not type(i) == list:
      c += 1
​
    else:
      c += get_length(i)
​
  return c

