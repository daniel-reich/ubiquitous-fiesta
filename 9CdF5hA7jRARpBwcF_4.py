
def map_letters(word):
  return {ch: [idx for idx, val in enumerate(word) if val == ch] for ch in word}

