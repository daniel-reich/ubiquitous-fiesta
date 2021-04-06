
def shift_letters(txt, n):
  nospace = txt.replace(" ", "")
  x = len(nospace)
  count = 0
  ans = ""
  for i in txt:
    if i == " ":
      ans += " "
    else:
      ans += nospace[(count-n)%x]
      count += 1
  return ans

