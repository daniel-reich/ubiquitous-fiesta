
def index_filter(indexes, string):
  newstr = ''
  for position in indexes:
    newstr += string.lower()[position]
  return newstr

