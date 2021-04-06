
def reverse(txt):
  return " ".join("".join(reversed(word)) if len(word)>4 else word for word in txt.split())

