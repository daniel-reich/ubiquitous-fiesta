
def special_reverse(s, c):
  return " ".join(i[::-1] if i.startswith(c) else i for i in s.split())

