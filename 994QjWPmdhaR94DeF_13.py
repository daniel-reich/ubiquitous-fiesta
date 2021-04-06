
def get_birthday_cake(name, age):
  if age % 2 == 0:
    str2 = "# " + str(age) + " Happy Birthday " + name + "! " + str(age) + " #"
    return [
    "#" * len(str2),
    str2,
    "#" * len(str2)
    ]
  elif age % 2 != 0:
    str3 = "* " + str(age) + " Happy Birthday " + name + "! " + str(age) + " *"
    return [
    "*" * len(str3),
    str3,
    "*" * len(str3)
    ]

