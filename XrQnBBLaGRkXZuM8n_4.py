
def index_filter(indexes, string):
  res = ''
  for x in indexes:
    res = res + string[x]
  return res.lower()

