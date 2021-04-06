
def alternating_caps(txt):
  count = 0
  mystr = ""
  for i in range (len(txt)):
    if (count%2==0 and txt[i]!=" "):
      mystr += txt[i].upper()
      count += 1
    elif (count%2!=0 and txt[i]!=" "):
      mystr += txt[i].lower()
      count += 1
    elif (txt[i]== " "):
      mystr += txt[i]
  return mystr

