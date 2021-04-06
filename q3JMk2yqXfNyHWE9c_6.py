
def double_letters(word):
  import re
  return len((re.compile(r'(\w)\1')).findall(word)) >= 1

