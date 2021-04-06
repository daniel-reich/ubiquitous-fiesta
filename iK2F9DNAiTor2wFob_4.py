
def calc(s):
  a = ''.join([str(ord(i)) for i in s])
  b = a.replace('7','1')
  a,b = sum(map(int,a)),sum(map(int,b))
  return a-b

