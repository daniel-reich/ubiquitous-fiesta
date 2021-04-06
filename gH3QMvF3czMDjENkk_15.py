
def remove_letters(letters, word):
  final = []
  for i in letters:
    if i not in word:
      final.append(i)
    elif i in word:
      if letters.count(i) > word.count(i):
        final.append(i)
        letters.remove(i)
  return final

