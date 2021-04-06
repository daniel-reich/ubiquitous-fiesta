
def greet_people(names):
  if names==[]: return ""
  for value, name in enumerate(names):
    names[value]= "Hello "+name
  return ", ".join(names)

