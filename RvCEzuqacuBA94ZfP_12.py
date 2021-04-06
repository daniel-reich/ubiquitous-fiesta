
def generate_hashtag(txt):
  txt = ''.join(word.capitalize() for word in filter(None, txt.split()))
  if not txt or len(txt) > 139:
    return False
  return '#' + txt

