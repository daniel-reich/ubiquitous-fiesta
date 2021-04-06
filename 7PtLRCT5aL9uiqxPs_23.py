
def last_dig(a, b, c):
  if sum([a,b,c]) == 3:
    return True 
  return str(int(str(a)[-1]) * int(str(b)[-1]))[-1] == str(c)[-1]

