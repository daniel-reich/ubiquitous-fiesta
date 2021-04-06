
def initialize(names):
  import re
  bla = [i.lower() for i in names]
  bla = [i.title() for i in bla]
  y = [re.sub(r'([a-z])','', bla[i]) for i in range(len(bla))]
  x = []
  for a in y:
    x.append(re.sub(r'([A-Z])', r'\1.', re.sub(r'[,:=/]', '', a)))
  return x

