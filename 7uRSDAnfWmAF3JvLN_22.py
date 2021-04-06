
def say_hello_bye(name, num):
  if num == 1:
    greeting = "Hello {}".format(name.capitalize())
  else:
    greeting = "Bye {}".format(name.capitalize())
    
  return greeting

