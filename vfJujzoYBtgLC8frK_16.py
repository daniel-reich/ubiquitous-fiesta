
def word_to_decimal(word):
    return int(
    word, 
    ord(max(word, key=str.casefold).lower()) - 86
  )

