
def text_to_num(phone):
  convert = {"ABC":2, "DEF":3, "GHI":4, "JKL":5, "MNO":6, "PQRS":7, "TUV":8, "WXYZ":9}
  return "".join(["".join([str(convert[j]) for j in convert if i in j]) if i.isalpha() else i for i in phone])

