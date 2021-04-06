
import re
def generate_hashtag(txt):
  if txt:
    A=re.findall(r'(?i)[a-z]+', txt)
    if A:
      res=''.join([x.capitalize() for x in A])
      return '#'+res if len(res)<140 else False
    else:
      return False
  else:
    return False

