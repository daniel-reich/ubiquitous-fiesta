
def reverse(txt):
  return " ".join(x[::-1] if len(x) > 4 else x for x in txt.split())

