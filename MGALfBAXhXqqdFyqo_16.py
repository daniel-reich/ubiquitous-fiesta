
def atbash(txt):
  low = "abcdefghijklmnopqrstuvwxyz"
  low_atb = "zyxwvutsrqponmlkjihgfedcba"
​
  NT = ''
  for i in txt:
    if i.islower():
      if i.isalpha():
        inx = low.index(i)
        NT += low_atb[inx]
      else:
        NT += i
    else:
      if i.isalpha():
        inx = low.index(i.lower())
        NT += low_atb[inx].upper()
      else:
        NT += i
  return NT

