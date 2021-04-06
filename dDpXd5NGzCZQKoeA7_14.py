
def num_args(func):
  c=0
  while True:
    try:
      func(*[i for i in range(c)])
      return c
    except:
      c+=1

