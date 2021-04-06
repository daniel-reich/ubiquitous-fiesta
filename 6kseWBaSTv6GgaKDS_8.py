
def next_letters(s,mem=1):
  d={chr(65+i):i for i in range(26)}
  rd={d[i]:i for i in d}
  lst=[d[i] for i in s[::-1]] if s!='' else [-1]
  res=[]
  for i in lst:
    res+=[rd[(i+mem)%26]]
    if i+mem>25:mem=(i+mem)//26
    else:mem=0
  if mem!=0:res+=[rd[mem-1]]
  return ''.join(res[::-1])

