
def accum(txt):
  result = ""
  for index in range(len(txt)):
    temp = txt[index].upper() + (txt[index].lower() * index)
    result += temp + "-"
  return result.strip("-")

