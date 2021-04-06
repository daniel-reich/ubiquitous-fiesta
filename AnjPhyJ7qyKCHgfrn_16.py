
def remove_vowels(string):
  return "".join(i if i not in "aeiou" else "" for i in string)

