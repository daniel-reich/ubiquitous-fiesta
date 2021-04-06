
import re
def increment_string(txt):
  return re.sub(r'(\d*)$', repl, txt)
  
def repl(match):
  s = match.group()
  return '1' if s == '' else str(int(s)+1).zfill(len(s))

