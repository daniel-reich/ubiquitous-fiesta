
def ascii_capitalize(txt):
  list = [letter for letter in txt]
  for i in range(len(list)):
    if ord(list[i])%2==0:
      list[i] = list[i].upper()
    else:
      list[i] = list[i].lower()
  return "".join(list)

