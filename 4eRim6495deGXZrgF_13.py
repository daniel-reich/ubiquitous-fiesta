
def column_chart(A, B, t):
  d = ['Mo','Tu','We','Th','Fr','Sa','Su']
  a=['  ']+[str(i*10) for i in range(1,max(t)//10+2)]
  b=['|']*len(a)
  res=[]
  res.append(a[::-1])
  res.append(b[::-1])
  for i in range(7):
    c=[d[i]]+['++']*(A[i]//10)+['**']*(B[i]//10)+['  ']*(t[i]//10-A[i]//10-B[i]//10)+['__']+['  ']*(len(a)-2-t[i]//10)
    res.append(c[::-1])
  res.append(b[::-1])
  res2=[' '.join(x) for x in zip(*res)]
  return '\n'.join(res2)

