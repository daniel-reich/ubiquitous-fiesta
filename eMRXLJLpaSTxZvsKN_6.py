
def is_ladder_safe(ldr):
  a=all([len(ldr[0])==len(i) for i in ldr]+[len(ldr[0])>=5])
  mem=''.join([str(i.count(' ')) for i in ldr]).split('0')
  b=all([mem[1]==i for i in mem[1:-1]]+[len(mem[1])<=2]) if len(mem)>1 else False
  c=mem==mem[::-1]
  return a and b and c

