
def generate_hashtag(txt):
  s="#{}".format("".join(txt.title().split()))
  if s=="#" or len(s)>140:
    return False
  return s

