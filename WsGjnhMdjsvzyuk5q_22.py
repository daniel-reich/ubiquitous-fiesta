
def dashed(txt):
  vows = "aeiouAEIOU"
  arr = []
  for c in txt:
    if c in vows:
      arr.append("-{0}-".format(c))
    else : arr.append(c)
  return "".join(arr)

