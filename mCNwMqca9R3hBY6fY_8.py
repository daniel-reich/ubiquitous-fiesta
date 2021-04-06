
def make_happy(txt):
  return "".join(txt[i] if txt[i] != '(' else ')' if txt[i-1] in ':;x8' else txt[i] for i in range(len(txt)))

