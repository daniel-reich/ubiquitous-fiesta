
def unrepeated(txt):
  text = []
  chars = set()
  for char in txt:
    if char not in chars:
      chars.add(char)
      text.append(char)
  return "".join(text)

