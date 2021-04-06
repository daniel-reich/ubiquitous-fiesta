
def say_hello_bye(name, num):
  if num == 1:
    return "Hello " + name.replace(name[0], name[0].upper())
  elif num == 0:
    return "Bye " + name.replace(name[0], name[0].upper())

