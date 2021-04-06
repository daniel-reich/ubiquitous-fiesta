
def secret(text):
  parts = text.split('*')
  res = "<" + parts[0] + "></" + parts[0] + ">"
  return res * int(parts[1])

