
def histogram(lst, char):
  st = ""
  for i in lst:
    if i != lst[-1]:
      st += i * char + "\n"
    else:
      st += i * char
  return st

