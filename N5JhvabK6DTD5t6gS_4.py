
import re
def markdown(symb):
  def do_markdown(s, m):
    return ' '.join(symb+w+symb if re.match(m, w, re.I) else w for w in s.split())
  return do_markdown

