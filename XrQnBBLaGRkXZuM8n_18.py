
def index_filter(indexes, string):
  return ''.join(list(map(lambda x:string[x].lower(), indexes)))

