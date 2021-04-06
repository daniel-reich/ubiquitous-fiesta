
def same_upsidedown(ntxt):
  if len(ntxt) == 1 and ntxt != "0":
    return False
  if ntxt == "0":
    return True
  flip = ntxt.replace("6", '%temp%').replace("9", "6").replace('%temp%', "9")
  return flip[::-1] == ntxt

