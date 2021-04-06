
def replace_vowel(word):
  dic = {"a":"1", "e":"2", "i":"3", "o":"4", "u":"5"}
  return "".join(dic[w] if w in dic.keys() else w for w in word)

