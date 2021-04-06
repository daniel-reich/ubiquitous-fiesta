
import re
def find_shortest_words(txt):
  A=re.findall('[a-zA-Z]+\'?\w{0,3}', txt)
  m=min(len(x) for x in A)
  return sorted([x.lower() for x in A if len(x)==m])

