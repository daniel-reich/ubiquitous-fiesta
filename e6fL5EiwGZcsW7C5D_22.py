
def alph_num(txt):
  result = ''
  for char in txt:
    result += str(ord(char)-65)+' '
  return result.strip()

