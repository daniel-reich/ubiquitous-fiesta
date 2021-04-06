
def consonants(word):
  return sum(1 for i in word.lower() if i not in "aeiou" and i.isalpha())
​
def vowels(word):
  return sum(1 for i in word.lower() if i in "aeiou")

