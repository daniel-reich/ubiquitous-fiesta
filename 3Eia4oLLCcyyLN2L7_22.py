
def remove_repeats(s):
  word = s[0]
  for i in range(1, len(s)):
    if s[i] != s[i-1]:
      word = word + s[i]
  return word

