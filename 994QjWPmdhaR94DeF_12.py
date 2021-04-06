
def get_birthday_cake(name, age):
  if age%2 == 0:
    string = "# {0} Happy Birthday {1}! {0} #".format(age, name)
    other_string = ""
    for x in string:
      other_string = other_string + "#"
  else:
    string = "* {0} Happy Birthday {1}! {0} *".format(age, name)
    other_string = ""
    for x in string:
      other_string = other_string + "*"
  return [other_string, string, other_string]

