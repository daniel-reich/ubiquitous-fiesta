
def dashed(txt):
  return ''.join(['-'+i+'-' if i in 'aeiouAEIOU' else i for i in txt])

