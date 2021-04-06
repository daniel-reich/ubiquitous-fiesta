
import re
def parse_code(txt):
  match_str = r'(?P<first_name>[a-zA-Z]*)0*(?P<last_name>[a-zA-Z]*)0*(?P<id>\w*)'
  m = re.match(match_str, txt)
  return m.groupdict()

