
def make_title(txt):
  output = ""
  arr = []
  for w in txt.split():
    brr = list(w)
    brr[0] = brr[0].upper()
    arr.append("".join(brr))
  return " ".join(arr)

