
def text_to_num(phone):
  texts = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
  convert = []
  for x in phone:
    if isinstance(x, str):
      for index, t in enumerate(texts):
        if x in t:
          x = str(index+2)
    convert.append(x)
  return "".join(convert)

