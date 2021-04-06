
def weekly_salary(hours):
  payment = 0
  
  for i in hours[0:5]:
    if i <= 8:
      payment = i*10 + payment
    else:
      payment = i*10 + (i-8)*5 + payment
      
  for i in hours[5:7]:
    if i <= 8:
      payment = i*10*2 + payment
    else:
      payment = 2*i*10 + 2*(i-8)*5 + payment
      
  return payment

