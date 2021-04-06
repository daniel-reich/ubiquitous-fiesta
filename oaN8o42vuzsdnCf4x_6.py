
def best_words(lst):
  m = max([score(word) for word in lst])
  return [word for word in lst if score(word) == m]
def score(word):
  keys = [chr(i) for i in range(97, 123)]
  vals = '13321424185231130111144840'
  dic = {k: (10 if v == '0' else int(v)) for k, v in zip(keys, vals)}
  return sum([dic[k] for k in word])

