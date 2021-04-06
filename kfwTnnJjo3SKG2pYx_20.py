
from re import sub
def replace_nums(string):
  return sub('\d+', lambda m: bin(int(m.group(0)))[2:], string)

