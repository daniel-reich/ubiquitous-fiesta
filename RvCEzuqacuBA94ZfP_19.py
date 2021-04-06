
def generate_hashtag(txt):
  txt = "".join(map(lambda word: word.capitalize(), txt.split(" ")))
  if len(txt) == 0:
    return False
  txt = "#" + txt
  if len(txt) > 140:
    return False
  return txt

