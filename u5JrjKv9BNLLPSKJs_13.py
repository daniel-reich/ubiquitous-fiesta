
def num_ways(n, s):
  n={n:1};c=0
  while n:
    mem={}
    for i in n:
      for j in s:
        if i-j==0:c+=n[i]
        elif i-j>0:
          if i-j not in mem:mem[i-j]=n[i]
          else:mem[i-j]+=n[i]
    n=mem
  return c

