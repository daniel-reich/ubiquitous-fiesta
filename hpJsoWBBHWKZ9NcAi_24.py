
import re
def bird_code(lst):
  def code(bird):
    names = re.sub(r'[-/]', ' ', bird).split()
    if   len(names) == 1:
      return names[0][:4].upper()
    elif len(names) == 2:
      return ''.join(n[:2] for n in names).upper()
    elif len(names) == 3:
      return '{0}{1}{2}'.format(names[0][0], names[1][0], names[2][:2]).upper()
    elif len(names) == 4:
      return ''.join(n[0] for n in names).upper()
      
  return list(map(code, lst))

