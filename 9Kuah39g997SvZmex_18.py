
def common_last_vowel(txt):
  get_last_vowel = lambda x: [ch for ch in x.lower() if ch in 'aeiou'][-1]
  lst = [get_last_vowel(word) for word in txt.split()]
  return max(lst,key=lst.count)

