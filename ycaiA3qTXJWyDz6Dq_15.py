
def consonants(word):
  vwls = 'aeiou' + 'aeiou'.upper()
  print([i for i in word if i not in vwls and i.isalpha()])
  return len([i for i in word if i not in vwls and i.isalpha()])
​
def vowels(word):
  vwls = 'aeiou' + 'aeiou'.upper()
  return len([i for i in word if i in vwls])

