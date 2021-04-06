
def formula(txt):
  if len(txt) == 0:
    return None
  else:
    txt = "".join(txt.split()).replace("a", "4").split("=")
    result = True
    for i in range(len(txt) - 1):
      if eval(txt[i]) != eval(txt[i + 1]):
        result = False
    return result

