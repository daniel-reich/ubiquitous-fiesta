
def index_filter(indexes, string):
  stringlist = ""
  for i in range(len(indexes)):
    stringlist += string[indexes[i]]
  return stringlist.casefold()

