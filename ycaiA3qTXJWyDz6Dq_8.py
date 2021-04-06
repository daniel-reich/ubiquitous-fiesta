
def consonants(word):
  return len([i for i in word.lower() if i.isalpha() and i not in "a,e,i,o,u" ])
​
def vowels(word):
  return len([i for i in word.lower() if i.isalpha() and i in "a,e,i,o,u" ])

