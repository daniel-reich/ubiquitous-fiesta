
import re
def comments_correct(txt):
  p=re.compile(r'(//)*?(/*[^.]*/)*?')
  if txt.count('/')%2==0 and txt.count('*')%2==0:
    return bool(p.search(txt))
  else:
    return False

