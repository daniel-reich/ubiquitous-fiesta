
def word_to_decimal(word):
  word = list(word.lower())
  base = ord(sorted(word)[-1]) - 86
  lst_base = [int(i, base) for i in word][::-1]
  return sum(i * base ** idx for idx, i in enumerate(lst_base))

