
def special_reverse(s, c):
  return " ".join([i[::-1] if i[0]==c else i for i in s.split()])

