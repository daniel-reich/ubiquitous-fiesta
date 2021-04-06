
def bird_code_word(w):
  w = ' '.join(w.split('-')).split(' ')
  if len(w) == 1: code = w[0][:4]
  if len(w) == 2: code = w[0][:2] + w[1][:2]
  if len(w) == 3: code = w[0][0] + w[1][0] + w[2][:2]
  if len(w) == 4: code = w[0][0] + w[1][0] + w[2][0] + w[3][0]
  return code.upper()
​
def bird_code(lst): return [bird_code_word(w) for w in lst]

