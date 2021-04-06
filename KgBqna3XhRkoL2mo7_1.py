
import re
def decrypt(s):
  for x in re.findall('..#',s):s=s.replace(x,chr(int(x[:-1])+96))
  return s.translate(s.maketrans('123456789','abcdefghi'))

