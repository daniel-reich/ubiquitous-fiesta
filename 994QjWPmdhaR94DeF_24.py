
def get_birthday_cake(name, age):
  c=""
  if age%2==0:
    c="#"
  if age%2!=0:
    c="*"
  mstr = c+" "+str(age)+" Happy Birthday "+name+"! "+str(age)+" "+c
  sides = c*len(mstr)
  return [sides,mstr,sides]

