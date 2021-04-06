
def is_alphabetically_sorted(sentence):
  return any([all([i[j+1]>=i[j] for j in range(len(i)-1)]) for i in sentence[:-1].split() if len(i)>=3])

