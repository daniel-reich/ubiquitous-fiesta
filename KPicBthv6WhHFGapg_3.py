
def count_syllables(txt):
  if not isinstance(txt, str):
    raise TypeError('txt need to be a str')
  return sum([txt.count(letter) for letter in 'aeyuioAEYUIO'])

