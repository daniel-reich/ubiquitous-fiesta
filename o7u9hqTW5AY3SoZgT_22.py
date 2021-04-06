
import string
def switcheroo(txt):
  l = txt.split()
  
  for i in range(len(l)):
    w = l[i].strip(string.punctuation)
    if "nts" in w[-3:]:
      l[i] = l[i].replace("nts", "nce")
    elif "nce" in w[-3:]:
      l[i] = l[i].replace("nce", "nts")
  
  return " ".join(l)

