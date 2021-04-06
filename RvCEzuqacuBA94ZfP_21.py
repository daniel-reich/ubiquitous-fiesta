
def generate_hashtag(txt):
  txt = ''.join(i.title() for i in txt.split())
  
  if not txt or len(txt) >= 140:
    return False
  return '#' + txt

