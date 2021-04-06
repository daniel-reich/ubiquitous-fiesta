
def reverse(txt):
  string = []
  for word in txt.split(" "):
    if len(word) >= 5:
      string.append(word[::-1])
    else:
      string.append(word)
  return " ".join(string)

