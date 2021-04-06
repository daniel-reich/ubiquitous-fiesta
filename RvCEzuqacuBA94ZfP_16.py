
from re import sub
def generate_hashtag(txt):
  txt = sub(r'(?<!\S)([a-z])',lambda x: x.group(1).upper(),txt)
  txt = sub(r'\s+','',txt)
  if len(txt) >= 139 or len(txt) == 0:
    return False
  return "#" + txt

