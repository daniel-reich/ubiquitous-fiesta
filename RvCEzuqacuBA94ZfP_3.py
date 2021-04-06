
def generate_hashtag(txt):
  lst = ''.join([i.capitalize() for i in txt.split(' ') if i != ''])
  return "#{}".format(lst) if lst and len(lst) < 140 else False

