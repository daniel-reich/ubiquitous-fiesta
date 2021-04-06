
def generate_hashtag(txt):
  txt = txt.title().replace(" ", "")
  return '#' + txt if 0 < len(txt) < 140 else False

