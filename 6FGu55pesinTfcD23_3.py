
def find_pattern(dict_, p):
  phrase = {True:p,False:"None"}
  phrases = []
  for key,val in dict_.items():
    phrases.append('{} = {}'.format(key,phrase[p in val]))
  return sorted(phrases)

