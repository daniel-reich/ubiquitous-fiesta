
def keyboard_mistakes(txt):
  conv = {"4": "A", "5": "S", "0": "O", "1": "I"}
  return "".join(conv[x] if x in conv else x for x in txt)

