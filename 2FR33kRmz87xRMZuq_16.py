
def histogram(lst, char):
  return ''.join(([i*char if i==lst[-1] else i*char+'\n' for i in lst]))

