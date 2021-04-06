
def generate_hashtag(txt):
  words = [w.capitalize() for w in txt.split()]
  if len(txt) == 0 or len(words) == 0: return False
  ret = "#" + "".join(words)
  if len(ret) > 140: return False
  return ret

