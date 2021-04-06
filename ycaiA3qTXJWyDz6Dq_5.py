
def consonants(word):
  return len([i for i in word.lower() if i not in 'aeiou' and i.isalpha()])
​
def vowels(word):
  return len([i for i in word.lower() if i in 'aeiou'])

