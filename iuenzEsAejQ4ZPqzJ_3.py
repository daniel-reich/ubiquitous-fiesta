
def mystery_func(num):
  s = [2**x for x in range(1,num)]
  for i in s:
    if num>i: c=s.index(i)+1
  return int(('2'*c)+str(num-(2**c)))

