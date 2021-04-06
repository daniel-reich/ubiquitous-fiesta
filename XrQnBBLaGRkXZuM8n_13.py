
def index_filter(indexes, string):
  word = ''
  for i in indexes:
    word += string[i]
  return word.lower()

