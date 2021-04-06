
def shared_letters(str1, str2):
  return len([x for x in set(str1) if x in set(str2)])

