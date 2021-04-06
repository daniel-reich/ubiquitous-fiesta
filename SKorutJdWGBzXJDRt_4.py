
def greet_people(names):
  list_greeting = []
  for n in names:
    list_greeting.append("Hello {0}".format(n))
  greet = ", ".join(list_greeting)
  return greet

