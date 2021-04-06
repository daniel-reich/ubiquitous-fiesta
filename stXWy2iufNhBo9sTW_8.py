
from string import ascii_uppercase as au
def valid_rondo(s):
  return len(s) >= 3 and len(s)&1 and set(s[0::2]) == set('A') and ''.join(s[1::2]) in au

