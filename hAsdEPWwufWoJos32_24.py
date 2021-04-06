
def no_yelling(phrase):
  if (phrase[-2:] == "!!"):
    return phrase.strip("!") + "!"
  elif (phrase[-2:] == "??"):
    return phrase.strip("?") + "?"
  else:
    return phrase

