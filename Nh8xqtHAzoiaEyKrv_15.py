
def correct_sentences(s):
  x = ' '.join(x for x in s.split())
  y = x[0].capitalize()
  print(x)
  for i in range(1,len(x) - 2):
    if (x[i + 2]).isupper():
      y += x[i] + '.'
    else:
      y += x[i]
  y += x[-2]
  if (x[-1] != ' '):
    y += x[-1]
  return y + '.'

