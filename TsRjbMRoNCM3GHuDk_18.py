
import re
def syllabification(word):
  vowel = "[aAeiou]"
  consonant = "[pbtdkgG?fvszSZxhcjmnrly]"
  syl = re.compile("{c}{v}{c}{{0,2}}(?!{v})".format(v=vowel, c=consonant))
  sylables = syl.findall(word)
  return '.'.join(sylables)

