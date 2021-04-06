
def split(number):
  if number==1:
    return 1
  elif number%3==1:
    return pow(3,number//3-1)*4
  elif number%3!=0:
    return pow(3,number//3)*(number%3)
  else:
    return pow(3,number//3)

