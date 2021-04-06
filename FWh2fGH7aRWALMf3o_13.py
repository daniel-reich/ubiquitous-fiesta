
def cleave(string, lst):
  lst = sorted(lst,key=len,reverse=True)
  res = []
​
  while len(string) != 0:
    val = 0
    for word in lst:
      if string.endswith(word):
        val = 1
        res.insert(0,word)
        string = string[:-len(word)]
        break
    if not val:
      return 'Cleaving stalled: Word not found'
  return ' '.join(res)

