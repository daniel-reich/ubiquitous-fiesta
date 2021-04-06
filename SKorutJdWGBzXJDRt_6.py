
def greet_people(names):
  greeting = ""
  for name in names:
    y = "Hello {}".format(name)
    greeting += y
    greeting += ", "
  greeting = greeting[:-2]
  return greeting

