
def absolute(txt):
  arr = []
  for w in txt.split():
    if w == "a":
      arr.append("an absolute")
    elif w == "A":
      arr.append("An absolute")
    else : arr.append(w)
  return " ".join(arr)

