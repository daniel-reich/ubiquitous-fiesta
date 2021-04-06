
def happy_birthday(age):
  is_20 = age % 2 == 0
  base = age/2 if is_20 else (age-1)/2
  fake_age = 20 if is_20 else 21
  return "Mubashir is just " + str(fake_age) + ", in base " + str(int(base)) + "!"

