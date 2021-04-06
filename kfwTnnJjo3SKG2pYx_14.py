
from re import sub
def replace_nums(string):
  return sub(r'(\d+)',lambda x: str(bin(int(x.group(1))))[2::],string)

