
def simple_numbers(a, b):
  return [i for i in range(a,b+1) if func(i)]
  
def func(n):
  return n==sum([int(str(n)[i])**(i+1) for i in range(len(str(n)))])

