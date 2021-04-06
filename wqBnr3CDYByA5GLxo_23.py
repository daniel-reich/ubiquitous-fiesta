
import re
import itertools
​
def generate(x):
  if len(x) >= 1 and x[0] == '[':
    elms = x[1:-1].split('|')
    for e in elms:
      yield e
  else:
    yield x
​
def unravel(txt):
  chunks = re.split(r'(\[.*?\])', txt)
​
  gens = []
  for c in chunks:
    gens.append([e for e in generate(c)])
​
  results = []
  for t in itertools.product(*gens):
    results.append(''.join(t))
​
  return sorted(results)

