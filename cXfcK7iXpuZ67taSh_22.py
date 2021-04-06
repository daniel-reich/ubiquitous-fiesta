
def mystery_func(txt):
  return ''.join(txt[i-1]*(int(txt[i])) for i in range(1,len(txt)+1,2))

