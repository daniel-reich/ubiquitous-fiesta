
def vowel_links(txt):
  import re
  lst=txt.split(' ')
  for i in range(len(lst)-1):
    if re.search("[aeiou]",lst[i][-1])and re.search("[aeiou]",lst[i+1][0]):
      return True
  return False

