
from functools import reduce
def text_to_num(phone):
  keypad = {"2": "ABC", "3": "DEF", "4": "GHI", "5": "JKL", "6": "MNO", "7": "PQRS", "8": "TUV", "9": "WXYZ"}
  for n, ls in keypad.items():
    phone = reduce(lambda s, l: s.replace(l, n), ls, phone)
  return phone

