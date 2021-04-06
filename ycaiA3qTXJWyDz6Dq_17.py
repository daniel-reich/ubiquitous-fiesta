
def consonants(word):
  return sum(1 for i in word if i.isalpha())-vowels(word)
​
def vowels(word):
    return sum(1 for i in word if i.lower() in "aeiou")

