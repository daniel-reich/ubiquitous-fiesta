
def absolute(txt):
  
  Sample = str(txt)
  
  if (txt[0] == "A") and (txt[1] == " "):
    Sample = Sample.replace("A ", "An absolute ")
    Sample = Sample.replace(" a "," an absolute ")
    Sample = Sample.replace(" A "," An absolute ")
    return Sample
  else:
    Sample = Sample.replace(" a "," an absolute ")
    Sample = Sample.replace(" A "," An absolute ")
    return Sample

