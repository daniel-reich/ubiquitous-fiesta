
import re;
def split_code(item):
  alphabets = re.findall(r'[a-zA-Z]+',item);
  digits = re.findall(r'\d+',item);
  return alphabets + [int(digits[0])];

