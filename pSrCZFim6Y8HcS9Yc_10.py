
def convert(deg):
  ans = deg.split('*')
  if '*' in deg :
    if ans[1] == "F" :
      a =  ((((int(ans[0])-32)*5))/9)
      a = round(a)
      return str(a)+ "*C"
    elif ans[1] == "C":
      b = ((int(ans[0]) * (9/5)) + 32)
      b = round(b)
      return str(b) + "*F"
  else:
    return "Error"
​
​
print(convert("35*C"))

