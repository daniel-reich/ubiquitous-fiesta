
def gimme_the_letters(s):
  return ''.join(list(map(chr,range(ord(s[0]), ord(s[-1])+1))))

