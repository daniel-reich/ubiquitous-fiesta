
def longest_nonrepeating_substring(txt):
  string = ''
  for i in range(len(txt)):
    cur_chars = []
    for j in txt[i:]:
      if j not in cur_chars:
        cur_chars.append(j)
      else: break
    if len(cur_chars) > len(string):
      string = ''.join(cur_chars)
  return string

