
def index_filter(indexes, string):
  return "".join([string[indexes[i]] for i in range(len(indexes))]).lower()

