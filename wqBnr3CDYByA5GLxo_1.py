
import re, itertools
def unravel(txt):
  lst = [i.strip('[]').split('|') for i in re.findall('[\w\s\'?]+|\[{1}[\s\w\'?\|]+\]{1}',txt)]
  return sorted([''.join(i) for i in itertools.product(*lst)])

