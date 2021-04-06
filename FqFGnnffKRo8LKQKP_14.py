
def simple(n):
  n = str(n)
  o=0
  for i in range(len(n)):
    o += int(n[i])**(i+1)
  return o==int(n)
​
def simple_numbers(a, b):
  return [i for i in range(a, b+1) if simple(i)]

