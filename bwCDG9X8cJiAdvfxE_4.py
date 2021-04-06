
def add_str_nums(num1,num2):
  result=-1
  if len(num1)==0:num1='0'
  if len(num2)==0:num2='0'
  if (num1.isnumeric()&num2.isnumeric()):
    x=int(num1);y=int(num2)
    result=x+y
  return(str(result))

