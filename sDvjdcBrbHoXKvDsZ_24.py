
def anagram(name, words):
  name = name.replace(" ","").lower()
  return sorted("".join(words)) == sorted(name)

