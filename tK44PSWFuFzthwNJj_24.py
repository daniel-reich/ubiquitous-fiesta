
from re import findall
def club_entry(txt):
  return (ord(findall(r'(.)\1', txt)[0]) - 96) * 4

