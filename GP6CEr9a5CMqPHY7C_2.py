
def words_to_sentence(words):
  try:
    words = [i for i in words if i != None or i if i != '']
    part1 = words[0:-1] + ['and'] + words[-1:]
    if len(words) == 2:
      return ' '.join(part1)
    if len(words) == 1:
      return words[0]
    if len(words) == 0:
      return ''
    return ', '.join(part1[0:-3])+ ', ' + ' '.join(part1[-3:])
  except:
      return ''

