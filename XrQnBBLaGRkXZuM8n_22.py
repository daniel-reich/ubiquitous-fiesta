
def index_filter(indexes, string):
  result = list(map(lambda i: string[i], indexes))
  convert = ''.join(result)
  return str.lower(convert)

