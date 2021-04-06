
def dial(txt):
  conversion = {
  'abc': '2',
  'def': '3',
  'ghi': '4',
  'jkl': '5',
  'mno': '6',
  'pqrs': '7',
  'tuv': '8',
  'wxyz': '9',
  }
  result = []
  for x in txt.lower():
    if x.isalpha(): result.extend(c[1] for c in conversion.items() if x in c[0])
    else: result.extend(x)
  return ''.join(result)

