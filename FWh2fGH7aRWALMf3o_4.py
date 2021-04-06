
def cleave(string, lst, tmp=[]):
  if len(string) == 0:
    return " ".join(tmp)
  else:
    for x in lst:
      if string.startswith(x):
        y = cleave(string[len(x):], lst, tmp + [x])
        if y != "Cleaving stalled: Word not found":
          return y
    return "Cleaving stalled: Word not found"

