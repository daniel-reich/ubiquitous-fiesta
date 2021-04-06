
def keyboard_mistakes(txt):
  obj = {"4": "A", "5": "S", "0": "O", "1": "I"}
  return "".join(obj[x] if x in obj else x for x in txt)

