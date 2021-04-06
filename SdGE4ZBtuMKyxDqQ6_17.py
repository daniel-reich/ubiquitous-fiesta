
def first_repeat(chars):
  s = ""
  for i in chars:
    if i not in s:
      s += i
    else:
      return i
  return "-1"

