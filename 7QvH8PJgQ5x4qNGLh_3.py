
def countdown(n, txt):
  words = ""
  for d in range(n, 0, -1):
    words = words + str(d) + ". "
  
  else:
    words += txt.upper()
    words += "!"
  
  return words

