
vowels = ['a', 'e', 'i', 'o', 'u']
​
def same_vowel_group(w):
  
  sameVowelsWords = []
​
  firstWordVowels = get_vowels(w[0])
  for i in range(len(w)):
    newWordVowels = get_vowels(w[i])
​
    if newWordVowels == firstWordVowels:
      sameVowelsWords.append(w[i])
​
  return sameVowelsWords
​
​
​
        
def get_vowels(word):
  usedVowels = []
​
  for letter in word:
    for vowel in vowels:
      if letter == vowel and vowel not in usedVowels:
        usedVowels.append(vowel)
        
  return sorted(usedVowels)

