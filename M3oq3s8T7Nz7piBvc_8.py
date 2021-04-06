
def even_odd_string(txt):
  return ''.join(txt[i] for i in range(len(txt)) if i % 2 == 0) + ' ' + ''.join(txt[i] for i in range(len(txt)) if i % 2 != 0)

