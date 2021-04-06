
import re
def same_length(txt):
    # I hate seeing the solutions
    # because they are
    #always so fking simple :)
  return [len(i) for i in re.findall('1+',txt)] == [len(i) for i in re.findall('0+',txt)]

