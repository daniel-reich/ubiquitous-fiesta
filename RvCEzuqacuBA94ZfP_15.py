
def generate_hashtag(txt):
  if txt == '':
    return False
  words = txt.split()
  if words == []:
    return False
  output = '#'
  for word in words:
    output += word.capitalize()
  if len(output) > 140:
    return False
  return output

