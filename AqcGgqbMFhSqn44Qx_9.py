
def tweet(txt):
  return ' '.join([i.replace('.', '').replace(',', '').replace('!', '').replace('?', '') for i in txt.split() if '#' in i or '@' in i])

