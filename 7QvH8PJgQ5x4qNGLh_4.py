
def countdown(n, txt):
  text = ""
  for i in range(n, 0, -1):
    text = text + str(i) + ". "
  return text+txt.upper()+"!"

