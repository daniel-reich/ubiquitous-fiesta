
def same_upsidedown(ntxt):
  upside_down = ""
  for char in ntxt[::-1]:
    if char == "6":
      upside_down += "9"
    elif char == "9":
      upside_down += "6"
    else:
      upside_down += char
  return ntxt == upside_down

