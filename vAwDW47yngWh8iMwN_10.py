
def cap_last(txt):
  lst = txt.split(" ")
  newstr = ""
  for x in lst:
    y = len(x)
    newstr = newstr + " " + x[:y - 1] + x[y - 1].upper()
  newstr = newstr.strip()
​
  return newstr

