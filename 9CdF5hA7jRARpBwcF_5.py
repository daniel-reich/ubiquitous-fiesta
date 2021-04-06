
def map_letters(word):
  id = [i for i in enumerate(word)]
  ky =  sorted(set(word),key=lambda i:word.index(i))
  return {k:[i[0] for i in id if i[1]==k] for k in ky}

