
def happy_birthday(age):
  if age % 2 == 0:
    return "Mubashir is just 20, in base " + str(int(age/2)) + "!"
  else:
    return "Mubashir is just 21, in base " + str(int((age-1)/2)) + "!"

