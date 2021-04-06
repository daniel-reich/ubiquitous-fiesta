
def letters(word1, word2):
  return [''.join(sorted(set(list(i   for i in word1  if i in word2)))), 
                    ''.join(sorted(set(list(i   for i in word1  if i  not in word2)))),
                    ''.join(sorted(set(list( i   for i in word2  if i not in word1))))]

