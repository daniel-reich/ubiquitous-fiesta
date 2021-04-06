
def generate_hashtag(txt: str):
  result = ''.join(map(str.capitalize, txt.split()))
  if len(result) == 0 or len(result) >= 140:
    return False
  return '#' + result

