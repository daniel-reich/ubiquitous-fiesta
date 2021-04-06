
def cap_space(txt):
  return "".join(char if char.islower() else " " + char.casefold() for char in txt)

