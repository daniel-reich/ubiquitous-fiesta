
def find_shortest_words(txt):
  lst = txt.split(' ')
  result = [i.strip('.').strip(',') for i in lst]
  l = 10000
  new_result =[]
  for j in result:
    if len(j) < l:
      l = len(j)
  for k in result:
    if len(k) == l and not k.isnumeric():
      new_result.append(k.lower())
  new_result.sort()
  return new_result

