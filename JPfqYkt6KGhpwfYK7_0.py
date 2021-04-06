
import re
def replace_the(txt):
  def repl(match):
    a,b = match.group(1,2)
    return ('an ' if b in 'aeiou' else 'a ') + b
  return re.sub('(the) (\w)', repl, txt)

