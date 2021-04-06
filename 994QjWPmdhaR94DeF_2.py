
def get_birthday_cake(name, age):
  val = "*" if age % 2 else "#"
  vals = val * (22 + len(str(age) * 2) + len(name))
  return [vals, "{0} {1} Happy Birthday {2}! {1} {0}".format(val, age, name), vals]

