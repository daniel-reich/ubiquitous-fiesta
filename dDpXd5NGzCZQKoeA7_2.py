
def num_args(func):
  on = True
  i = 0
  while on:
    try:
      func(*([1]*i))
      on = False
    except:
      i+= 1
  return i

