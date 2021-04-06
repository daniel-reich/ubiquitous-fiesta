
def no_yelling(phrase):
  while phrase[-2] == '!' or phrase[-2] == '?':
    phrase = phrase[0:-1]
  
  return phrase

