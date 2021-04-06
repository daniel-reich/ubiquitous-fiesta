
def split(txt):
  def is_vowel(let):
    return let in 'aieou'
  return ''.join([let for let in txt if is_vowel(let)] + [let for let in txt if not is_vowel(let)])

