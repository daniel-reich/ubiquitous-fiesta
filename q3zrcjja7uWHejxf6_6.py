
def negative_sum(chars):
  def clean(chars):
    for char in chars:
      try:
        i = int(char)
      except ValueError:
        if char != '-':
          chars = chars.replace(char,':')
    
    for n in range(10):
      if '{}-'.format(n) in chars:
        chars = chars.replace('{}-'.format(n), '{}:-'.format(n))
    
    return ''.join([c for c in chars if c != ''])
  
  cleaned = clean(chars)
  ints = [int(i) for i in cleaned.split(':') if i != '']
  
  return sum([i for i in ints if i < 0])

