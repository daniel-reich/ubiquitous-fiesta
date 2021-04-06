
def no_yelling(phrase):
  if phrase[-1] not in "!?":
    return phrase
  punct = phrase[-1]
  lst = phrase.split()
  return " ".join(lst[:-1]+[lst[-1].replace(punct, "")+punct])

