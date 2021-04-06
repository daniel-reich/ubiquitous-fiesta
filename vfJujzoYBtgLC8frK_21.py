
def word_to_decimal(word):
  word = word.lower()
  base = ord(max(word))-86
  final = 0
  for i in range(len(word)):
    final+=(ord(word[i])-87)*pow(base,len(word)-i-1)
  return final

