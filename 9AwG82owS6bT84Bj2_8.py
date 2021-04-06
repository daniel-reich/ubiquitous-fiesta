
def doubled_pay(n):
  dosh = 1
  pay=1
  if n == 1:
    pass
  else:
    for i in range(1,n):
      pay *= 2
      dosh += pay
  return dosh

