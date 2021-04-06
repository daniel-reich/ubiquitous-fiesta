
def count_smileys(lst):
  counter=0
  import re
  pattern = re.compile("(?::|;|a^)(?:-|~|a^)?(?:\)|D|a^)")
  for i in lst:
    if re.match(pattern,i):
      counter+=1
  return counter

