
import re
def decrypt(s):
  string = 'abcdefghijklmnopqrstuvwxyz'
  return re.sub(r'(\d)',lambda x: string[int(x.group(1))-1],re.sub(r'(\d{2})(#)',lambda x: string[int(x.group(1))-1],s))

