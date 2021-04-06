
def word_to_decimal(word):
  alpha = "abcdefghijklmnopqrstuvwxyz"
  base = alpha.index(sorted(word.lower())[-1])+11
  return sum([(alpha.index(word[i].lower())+10) * (base**(len(word)-i-1)) for i in range(len(word))])

