
def simple_encoder(s):
  alt_text = [i.lower() for i in s]
  return "".join(["[" if alt_text.count(i) == 1 else "]" for i in alt_text])

