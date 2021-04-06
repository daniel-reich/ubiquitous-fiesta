
def generate_hashtag(txt):
  ret = '#'+''.join([i.capitalize() for i in txt.split()])
  return ret if 1<len(ret)<140 else False

