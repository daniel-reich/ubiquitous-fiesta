
def inator_inator(inv):
  length = len(inv)
  vowels = 'aeiou'
  if inv[length-1:length].lower() in vowels: inv += '-'
  inv += 'inator {}000'.format(length)
  return inv

