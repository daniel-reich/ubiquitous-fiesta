
from re import sub
def hidden_anagram(s, t):
  s, t = sub('[^a-z]','', s.lower()), sorted(sub('[^a-z]','',t.lower()))
  for i in range(len(s)):
    if ''.join(sorted(s[i:i+len(t)])) == ''.join(t):return s[i:i+len(t)]
  return 'noutfond'

