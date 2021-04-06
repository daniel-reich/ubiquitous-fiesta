
def happy_birthday(age):
  for x in range(2, age):
    a, b=divmod(age,x)
    if 10*a+b==20:
      return "Mubashir is just 20, in base {}!".format(x)
    if 10*a+b==21:
      return "Mubashir is just 21, in base {}!".format(x)

