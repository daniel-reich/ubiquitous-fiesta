
def generate_hashtag(txt):
  hashtag = "#"
  print(txt)
  txt = txt.split()
  print(type(txt))
  if not txt:
    return False
  for i in range(len(txt)):
    txt[i] = txt[i].replace(txt[i], txt[i].lower())
  for i in range(len(txt)):
    txt[i] = txt[i].replace(txt[i][0], txt[i][0].upper(),1)
  for s in txt:
    hashtag += s
  if len(hashtag) > 140:
    return False
  print(hashtag)
  return hashtag

