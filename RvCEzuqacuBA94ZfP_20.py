
def generate_hashtag(txt):
  strip_txt = txt.strip()
  if strip_txt == '':
    return False
  split_txt = strip_txt.split(' ')
  merge_txt = ''
  for i in split_txt:
    if i != '':
      merge_txt += i.capitalize()
  hash_txt = '#'+merge_txt
  if len(hash_txt) > 140:
    return False
  return hash_txt

