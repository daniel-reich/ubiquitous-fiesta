
def happy_birthday(age):
  for i in range(1,150):
    if divmod(age,i) in [(2,0),(2,1)]:
      return "Mubashir is just {}, in base {}!".format("{}{}".format(*list(divmod(age,i))),i)
  return None

