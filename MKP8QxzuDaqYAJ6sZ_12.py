
import re
def is_correct_aliases(names, aliases):
  return all(re.match(r'^{}\w+ {}\w+$'.format(names[i][0], names[i][0]), aliases[i]) \
    for i in range(len(names)))

