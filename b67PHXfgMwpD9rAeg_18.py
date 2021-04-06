
import re
def plus_sign(string):                    # Know your neighbor
  return len(re.findall(r'(?=\+.?([a-zA-Z]).?\+)', string)) == len([x for x in string if x.isalpha()])

