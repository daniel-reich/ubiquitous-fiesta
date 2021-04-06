
def common_last_vowel(txt):
  last_v = [[x for x in word[::-1] if x in 'aeiou'][0:1] for word in txt.lower().split()]
  return max(last_v, key= lambda x: last_v.count(x))[0]

