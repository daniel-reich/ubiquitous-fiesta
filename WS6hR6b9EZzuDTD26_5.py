
def no_duplicate_letters(phrase):
  from collections import Counter
  split = phrase.split()
  array = map(lambda x: Counter([i.lower() for i in x]).most_common(1)[0][1], split)
  if max(list(array)) > 1:
    return False
  else:
    return True

