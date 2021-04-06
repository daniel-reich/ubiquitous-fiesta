
def mystery_func(txt):
  string = ''
  for index in range(0,len(txt),2):
    string += txt[index] * int(txt[index+1])
  return string

