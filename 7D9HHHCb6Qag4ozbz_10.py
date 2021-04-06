
def find_zip(txt):
  if txt.count("zip")>1:
    a=txt.find("zip")
    b=txt.find("zip",a+1)
    return b
  else: return -1

