
from re import sub, I
def find_longest(s, w=None):
  return find_longest(sub(r"[^a-z]", "|", s, flags=I).split("|"), "") if w is None \
    else find_longest(s[1:], [w, s[0]][len(s[0]) > len(w)]) if len(s) else w.lower()

