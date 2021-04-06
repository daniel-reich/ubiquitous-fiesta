
def truncate(txt, length):
  if length >= len(txt):
    return txt
  else:
    words = txt[:length+1].count(" ")
    tmpTXT = txt.split()
    return " ".join(tmpTXT[:words])

