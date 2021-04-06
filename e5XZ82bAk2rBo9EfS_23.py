
def bed_time(*times):
  res=[]
  for i in times:
    a,b = zip(i[0].split(':'),i[1].split(':'))
    h=(int(a[0])-int(a[1])+(int(b[0])-int(b[1]))//60)%24
    m=(int(b[0])-int(b[1]))%60
    res+=['{:0>2}:{:0>2}'.format(h,m)]
  return res

