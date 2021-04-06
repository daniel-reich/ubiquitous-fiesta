
def reverse(arg):
  if str(arg) == "0" or str(arg) == "1":
    return "boolean expected"
  return not arg if arg == True or arg == False else "boolean expected"

