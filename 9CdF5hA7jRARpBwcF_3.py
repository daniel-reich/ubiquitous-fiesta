
def map_letters(word):
  return  {j: [i for i in range(len(word)) if word[i] == j] for j in word}

