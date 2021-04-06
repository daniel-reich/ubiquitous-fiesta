
from itertools import takewhile
 
def lcp(*s):
    return ''.join(ch[0] for ch in takewhile(lambda x: min(x) == max(x),
               zip(*s)))
​
def look_and_say(start, n):
  if n == 1:
    return [start]
  s = str(start)
  if len(s) == 1:
    return [start] + look_and_say(int('1' + s), n-1)
  l = []
  while s:
    cnt = len(lcp(s, s[0] * len(s)))
    l.append((str(cnt), s[0]))
    s = s[cnt:]
  return [start] + look_and_say(int(''.join(a + b for a, b in l)), n-1)

