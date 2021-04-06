
def alph_num(txt):
  result = ""
  for char in txt:
    result += str(ord(char) - ord("A")) + " "
  return result[:-1]

