
import string
def missing_letter(txt):
  txt = sorted(txt)
  lowercase = list(string.ascii_lowercase)
  first_index = lowercase.index(txt[0])
  y = lowercase[first_index: first_index + len(txt)]
  for i in range(len(y)):
    if y == txt:
      return 'No Missing Letter'
    elif y[i] == txt[i]:
      continue
    else:
      return y[i]

