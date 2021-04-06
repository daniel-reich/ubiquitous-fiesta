
def vowel_links(txt):
  return any(txt.split()[i][-1] in 'aeiou' and txt.split()[i+1][0] in 'aeiou' for i in range(len(txt.split())-1))

