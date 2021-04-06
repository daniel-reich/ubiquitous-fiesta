
def simplify_frac(f):
  lst = [int(i) for i in f.split("/")]
  a=lst[0]
  b=lst[1]
  alst=[a]
  blst=[]
  for x in range(1,a):
    if a % x == 0:
      alst.append(x)
  for y in range(1,b):
    if b % y == 0:
      blst.append(y)
  reslst=[i for i in blst if i in alst]
  answer=[str(int(i/reslst[-1])) for i in lst]
  return "/".join(answer)

