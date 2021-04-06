
def mystery_func(txt):
  lst = list(txt)
  string = ''
  x = 0
  for i in range(0, len(txt)-1, 2):
    x = int(lst[i+1])
    string += lst[i] * x
  return string

