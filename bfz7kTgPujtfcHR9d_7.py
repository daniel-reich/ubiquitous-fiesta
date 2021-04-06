
import re
def x_pronounce(sentence):
  s1=re.sub('(?<=\s)x(?=\s)', 'ecks', sentence)
  s2=re.sub('(?<=[aeiou])x', 'cks', s1)
  s3=re.sub('x(?=[ay])', 'z', s2)
  return s3

