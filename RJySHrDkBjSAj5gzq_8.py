
def nespers(lst):
  f,prod = lambda x: f(x-1)*x if x else 1, lambda x: eval("*".join(x))
  return f(len(lst))*prod(str(nespers(i)) for i in lst+[0]) if type(lst)==list else 1

