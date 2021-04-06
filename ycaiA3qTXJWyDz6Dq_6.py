
def consonants(word):
  return len([i for i in word.lower() if (i.isalpha() and i not in 'aoeiu')])
​
def vowels(word):
  return sum([1 for i in word.lower() if i in 'aoeiu'])

