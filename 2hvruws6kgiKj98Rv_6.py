
def to_scottish_screaming(txt):
  vowels = 'aieou'
  return ''.join(
    char.upper() if char.lower() not in vowels else 'E'
    for char in txt
  )

