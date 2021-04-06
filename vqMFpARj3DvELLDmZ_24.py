
def letters_only(txt):
  return "".join(c for c in txt if ord("a")<=ord(c.lower())<=ord("z"))

