
def anagram(name, words):
  first = "".join(sorted(name.lower().replace(" ","")))
  second = "".join(sorted("".join(words)))
  if len(first) == len(second):
    if first in second:
      return True
  else:
    return False

