
def remove_vowels(txt):
  ans = []
  key = list('aeiouAEIOU')
  for i in txt:
    if not i in key:
      ans.append(i)
  return ''.join(ans)

