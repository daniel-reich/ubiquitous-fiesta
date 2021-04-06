
import re
def eadibitan(word):
  vo = 'aeiouAEIOU'
  vow = 'aeiouAEIOUyY'
  conv = lambda s: re.sub('^([^{0}])([^{0}]?[{0}yY])'.format(vo), r'\2\1', s.group(0))
  return re.sub('[^{0}]{{0,2}}[{0}]{{1,3}}(?:[^{0}](?![{0}]))?'.format(vow), conv, word)

