
def consonants(word):
  count = 0
  vow = "aeiou"
  for i in word.lower():
    if i not in vow and i.isalpha():
      count += 1
  return count
​
def vowels(word):
  vow = "aeiou"
  count = 0
  for i in word.lower():
    if i in vow:
      count += 1
  return count

