
def seven_boom(lst):
  import re
  if re.search("7", str(lst)) != None:
    return ("Boom!")
  else : return ("there is no 7 in the list")

