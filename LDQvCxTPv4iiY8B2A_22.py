
def same_upsidedown(ntxt):
  flipedNum = ""
  num = ntxt[::-1]
  for el in num:
    if el == "6":
      flipedNum += "9"
    elif el == "9":
      flipedNum += "6"
    else:
      flipedNum += "0"
  return flipedNum == ntxt

