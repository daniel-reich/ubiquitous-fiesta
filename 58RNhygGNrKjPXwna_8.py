
def longest_nonrepeating_substring(txt):
  subs = []
  current =''
  while txt != '':
    for i in txt:
      if i not in current:
        current += i
      else:
        subs.append(current)
        current = '' + i
    subs.append(current)
    current = ''
    txt = txt[1::]
  return max(subs , key = len)

