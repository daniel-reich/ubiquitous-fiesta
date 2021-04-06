
def same_upsidedown(ntxt):
  def swap69(txt):
    return txt.replace("6", "x").replace("9", "6").replace("x", "9")
  if ntxt == "0":
    return True
  if len(ntxt) % 2 and ntxt[len(ntxt)//2] != "0":
    return False
  first_half = ntxt[:(len(ntxt)//2)]
  second_half = ntxt[-(len(ntxt)//2):]
  return  first_half == swap69(second_half[::-1])

