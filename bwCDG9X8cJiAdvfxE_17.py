
def add_str_nums(num1, num2):
  try:
    n=int(num1)
    n2=int(num2)
    return str(n+n2)
  except:
    if(num1 == ''):
      n=0
    if(num2 == ''):
      n2=0
    if(num1!='' and num2!=''):
      return '-1'
    else:
      return str(n+n2)

