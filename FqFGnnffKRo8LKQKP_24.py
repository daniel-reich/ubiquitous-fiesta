
def simple_numbers(a, b):
  return [x for x in list(range(a,b+1)) if or_not(x)];
def or_not(x):
  arr = list(str(x))
  return sum([int(i)**(j+1) for j,i in enumerate(arr)])==x

