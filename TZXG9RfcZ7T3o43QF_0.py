
import re
def same_length(txt):
  return [len(i) for i in re.findall('1+',txt)]==[len(i) for i in re.findall('0+',txt)]

