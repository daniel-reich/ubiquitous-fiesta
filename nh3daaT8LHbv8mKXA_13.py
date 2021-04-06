
import re
def text_to_num(phone):
  dicti = {'ABC': '2', 'DEF': '3', 'GHI': '4', 'JKL':'5', 'MNO':'6', 'PQRS':'7','TUV': '8', 'WXYZ':'9' }
  for k,v in dicti.items():
    for char in k:
      phone = re.sub(char,v, phone )
  return phone

