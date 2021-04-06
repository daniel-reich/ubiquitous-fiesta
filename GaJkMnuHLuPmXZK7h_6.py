
def letters(word1, word2):
  bot = ''
  wo1 = ''
  wo2 = ''
  for x in 'abcdefghijklmnopqrstuvwxyz':
    if x in word1 and x in word2:
      bot += x
    elif x in word1 and x not in word2:
      wo1 += x
    elif x not in word1 and x in word2:
      wo2 += x
    else:
      pass
  return [bot, wo1, wo2]

