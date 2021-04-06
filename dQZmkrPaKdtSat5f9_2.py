
def single_occurrence(txt):
  ans = txt.upper()
  if txt:
    for i in ans:
      if ans.count(i) == 1:
        return i
  return ''

