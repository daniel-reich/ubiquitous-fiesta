
def f(a):
  return sum(map(f,a))+1 if type(a)==list else 1
deep_count=lambda l:f(l)-1

