
def cap_last(txt):
  return " ".join(''.join(start) + end.upper() for *start, end in txt.split())

