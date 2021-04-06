
def comments_correct(txt):
  for i in range(0, len(txt), 2):
    if (txt[i:i+2] == '*/' and txt[i-2:i] != '/*') or (txt[i:i+2] == '/*' and txt[i+2:i+4] != '*/') or (len(txt) % 2 != 0):
      return(False)
  return(True)

