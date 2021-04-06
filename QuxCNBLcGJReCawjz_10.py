
def palindrome_type(n):
  binar = format(n, 'b')
  num = str(n)
  revBinar = ""
  revNum = ""
​
  for x in num:
    revNum = x + revNum
​
  
  for x in binar:
    revBinar = x + revBinar
​
  
​
  if binar == revBinar and num == revNum :
    return ("Decimal and binary.")  
  else:
    if num == revNum :
      return ("Decimal only.")  
    elif binar == revBinar:
      return ("Binary only.") 
    else:
      return ("Neither!")

