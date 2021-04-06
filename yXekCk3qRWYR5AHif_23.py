
VOWELS = set("aeiou")
​
def vow_replace(word, vowel):
  return "".join(vowel if c in VOWELS else c for c in word)

