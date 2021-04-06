
def get_drink_ID(flavor, ml):
  res = ""
  for word in flavor.split(' '):
    res += "".join(word[:3]).upper()
  res += ml.split("m")[0]
  return res

