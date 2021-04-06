
def replace_the(txt):
  x = txt.split(' ')
  return ' '.join('an' if (x[i] == 'the' and x[i+1][0] in 'aeiou') else 'a' if x[i] == 'the' else x[i] for i in range(0, len(x) - 1)) + ' ' + x[-1]

