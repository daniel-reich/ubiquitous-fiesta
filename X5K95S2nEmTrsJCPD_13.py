
def emotify(txt):
  if txt.find("smile") != -1:
    return(txt.replace("smile", ":D"))
  elif txt.find("grin") != -1:
    return(txt.replace("grin", ":)"))
  elif txt.find("sad") != -1:
    return(txt.replace("sad", ":("))
  else:
    return(txt.replace("mad", ":P"))

