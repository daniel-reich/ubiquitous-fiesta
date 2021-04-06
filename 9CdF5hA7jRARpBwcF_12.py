
def map_letters(word):
  dic = {}
  for i in range(len(word)):
    if word[i] not in dic.keys(): dic[word[i]] = [i]
    else: dic[word[i]].append(i)
  return dic

