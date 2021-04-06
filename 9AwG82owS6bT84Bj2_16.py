
def doubled_pay(n):
  def pay_day(n):
    if n == 1:
      return 1
    else:
      return pay_day(n-1) * 2
  
  pay = 0
  
  for num in range(1, n+1):
    pay += pay_day(num)
    #print(num, pay_day(num))
  
  return pay

