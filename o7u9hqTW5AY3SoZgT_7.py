
def switcheroo(txt):
  txt = txt.split(" ")
  for i in range(len(txt)):
      w = "".join([k for k in txt[i] if k.isalpha()])
      if "nts" in w:
          if w[-3:] == "nts":
              txt[i] = txt[i].replace("nts", "nce")
      elif "nce" in w:
          if w[-3:] == "nce":
              txt[i] = txt[i].replace("nce", "nts")
  return " ".join(txt)

