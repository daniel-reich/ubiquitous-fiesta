
def get_birthday_cake(name, age):
  bg = " "
  if age % 2 == 0:
    bg = "#"
  if age % 2 != 0:
    bg = "*"
  middle = "{} {} Happy Birthday {}! {} {}".format(bg, age, name, age, bg)
  borders = bg * len(middle)
  return [borders, middle, borders]

