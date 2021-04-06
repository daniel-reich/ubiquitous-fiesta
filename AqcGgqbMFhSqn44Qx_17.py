
def tweet(txt):
  return ' '.join(x.strip('.,!?') for x in txt.split(' ') if x[0] == '#' or x[0] == '@')

