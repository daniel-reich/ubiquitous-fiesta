
def generate_hashtag(txt):
  
  while '  ' in txt:
    txt = txt.replace('  ', ' ')
  
  if len(txt) == 0 or txt.count(' ') == len(txt):
    return False
  
  words = [word.capitalize() for word in txt.split(' ')]
  
  hashtag = '#' + ''.join(words)
  
  return hashtag if len(hashtag) <= 140 else False

