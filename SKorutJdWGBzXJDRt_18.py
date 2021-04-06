
def greet_people(names):
  greeting = ""
  for i in names:
    greeting += "Hello " + i + ", "
  return greeting[0:len(greeting)-2]

