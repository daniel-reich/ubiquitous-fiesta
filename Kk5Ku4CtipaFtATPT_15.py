
def coconut_translator(txt):
  txt = [bin(i)[2:].zfill(8) for i in bytearray(txt, "utf8")]
  output = ""
  for i in txt:
    for j, k in zip(i, "coconuts"):
      if j == "1":
        output += k.upper()
      else:
        output += k
    output += " "
  return output.strip()

