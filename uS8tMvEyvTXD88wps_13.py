
def reverse(txt):
  return ' '.join([word[::-1] if len(word)>4 \
  else word for word in txt.split()])

