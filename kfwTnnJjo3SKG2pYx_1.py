
import re
def replace_nums(string):
  return re.sub( r'\d+',
                lambda match: '{:b}'.format(int(match.group(0))),
                string)

