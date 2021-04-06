
def reverse(txt):
  out = ""
  split = txt.split(" ")
  for i in split:
    if len(i) >= 5:
      out += i[::-1] + " "
    else:
      out+= i + " "
  return out[:-1]

