
def int_to_str(arg):
​
  count,rs = arg, ""
​
  while count > 0:
    if count >= 1000:
      rs+='M'
      count-=1000
    elif count >= 900:
      rs+='CM'
      count-=900
    elif count >= 500:
      rs+='D'
      count-=500
    elif count >= 400:
      rs+='CD'
      count-=400
    elif count >= 100:
      rs+='C'
      count-=100
    elif count >= 90:
      rs+='XC'
      count-=90
    elif count >= 50:
      rs+='L'
      count-=50
    elif count >= 10:
      rs+='X'
      count-=10
    elif count >= 9:
      rs+='IX'
      count-=10
    elif count >= 5:
      rs+='V'
      count-=5
    elif count >= 4:
      rs+='IV'
      count-=4
    elif count >= 1:
      rs+='I'
      count-=1
  return rs
def str_to_int(arg):
  result=0
  a=arg.replace('IV','IIII')
  b=a.replace('IX','VIIII')
  c=b.replace('XL','XXXX')
  d=c.replace('XC','LXXXX')
  for letters in d:
    if letters=='M':
      result+=1000
    elif letters=='D':
      result+=500
    elif letters=='C':
      result+=100
    elif letters=='L':
      result+=50
    elif letters=='X':
      result+=10
    elif letters=='V':
      result+=5
    elif letters=='I':
      result+=1
  return result
def roman_numerals(arg):
  if type(arg) == int:
    return(int_to_str(arg))
  else:
    return(str_to_int(arg))

