
def best_friend(s, a, b):
  return s != a if len(s) == 1 else False \
    if s[0] == a and s[1] != b else best_friend(s[1:], a, b)

