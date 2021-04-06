
def correct_sentences(s):
  s=s.split()
  for i in range(len(s)):
    if s[i][0].isupper():
      s[i-1]=s[i-1]+'.'
  s[0]=s[0].capitalize()
  s[-1]=s[-1]+'.'
  return ' '.join(s)

