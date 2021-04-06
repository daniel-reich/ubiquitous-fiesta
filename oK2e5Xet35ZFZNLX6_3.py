
def neighboring(txt):
  char_codes = [ord(txt[i]) for i in range(len(txt))]
  return all([abs(x - char_codes[idx]) == 1 for idx, x in enumerate(char_codes[1:])])

