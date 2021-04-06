
def missing_alphabets(txt):
  string = 'abcdefghijklmnopqrstuvwxyz'
  freq = {x: txt.count(x) for x in string}
  k = max(list(freq.values()))
  return ''.join(list(map(lambda x: (k - freq[x]) * x, string)))

