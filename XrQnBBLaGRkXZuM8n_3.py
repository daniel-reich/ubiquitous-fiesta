
def index_filter(indexes, string):
  string2 = []
  for i in indexes:
    string2.append(string[i].lower())
  return ''.join([str(elem) for elem in string2])

