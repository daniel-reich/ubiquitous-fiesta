
from collections import Counter
def can_build(txt1, txt2):
  c1 = Counter(''.join(txt1.split()))
  c2 = Counter(''.join(txt2.split()))
  return len(c1-c2)==0

