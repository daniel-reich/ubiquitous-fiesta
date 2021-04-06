
def add_letters(a):
  val = sum([ord(i) - 96 for i in a])
  return "z" if not a else chr(val + 96) if val < 27 else chr((val % 26) + 96)

