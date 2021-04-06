
def happy_birthday(age):
  base = age // 2
  result = 20 if age % 2 == 0 else 21
  return "Mubashir is just {result}, in base {base}!".format(result=result, base=base)

