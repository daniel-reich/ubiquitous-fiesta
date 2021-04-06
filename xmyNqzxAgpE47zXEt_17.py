
def is_alphabetically_sorted(sentence):
  words = [word for word in sentence.split() if len(word)>=3]
  words = [word if word[-1] != "." else word[:-1] for word in words]
  res = []
  for word in words:
    res.append(all([word[i] <= word[i+1] for i in range(len(word)-1)]))
  return any(res)

