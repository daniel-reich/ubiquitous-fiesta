
import re
initial = re.compile(r'\A[A-Z]\.\Z')
name = re.compile(r'\A[A-Z][a-z]+\Z')
def valid_name(txt):
  def identify(s):
    if bool(initial.match(s)):
      return 1
    if bool(name.match(s)):
      return 2
    return -1
  return [identify(i) for i in txt.split()] in [[1,2],[1,1,2],[2,1,2],[2,2,2]]

