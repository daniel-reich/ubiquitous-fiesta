
import re
def direction(lst):
  out = []
  for w in lst:
    repl = {'e':'w','E':'W','a':'e','A':'E'}
    patt = re.compile("|".join(repl.keys()))
    out.append(patt.sub(lambda x: repl[x.group()], w))
  return out

