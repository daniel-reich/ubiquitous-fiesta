
def sort_by_last(txt):
  collector = dict()
  
  for word in txt.split(' '):
    if word[-1] not in collector.keys():
      collector[word[-1]] = [word]
    else:
      collector[word[-1]] = collector[word[-1]] + [word]
  
  result = list()
  
  for key in sorted(collector.keys()):
    for word in collector[key]:
      result.append(word)
      
  return ' '.join(result)

