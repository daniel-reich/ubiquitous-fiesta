
def calc(s):
  t1=''
  for x in s:
    t1+=str(ord(x))
  t2=t1.replace('7','1')
  return sum(int(x) for x in t1)-sum(int(x) for x in t2)

