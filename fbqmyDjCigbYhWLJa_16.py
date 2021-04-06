
import re
def split_into_buckets(phrase, n):
  first = re.findall(r'^\S+',phrase)[0]
  words = re.findall(r'\s\S+',phrase)
  if len(first) > n:
    return []
  else:
    lst = [first]
    for word in words:
      if len(lst[-1]) + len(word) > n:
        lst.append(word[1::])
      else:
        lst[-1] += word
  return lst

