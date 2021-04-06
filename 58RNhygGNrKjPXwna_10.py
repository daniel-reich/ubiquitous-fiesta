
def longest_nonrepeating_substring(txt):
  count = 0
  string = ""
  for i in range(len(txt)):
    for j in range(i, len(txt)):
      if len(set(txt[i:j+1])) == len(txt[i:j+1]):
        if len(txt[i:j+1]) > count:
          count, string = len(txt[i:j+1]), txt[i:j+1]
  return string

