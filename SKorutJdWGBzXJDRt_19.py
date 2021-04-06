
def greet_people(names):
  greeting = []
  for name in names:
    name = "Hello " + name 
    greeting.append(name)
  return ", ".join(greeting)

