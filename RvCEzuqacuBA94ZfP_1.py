
def generate_hashtag(txt):
  res = '#'
  for i in txt.split():
    res+=i[0].upper()+i[1:]
  return res if 1<len(res)<=140 else False

