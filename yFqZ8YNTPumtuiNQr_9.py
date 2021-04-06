
import re
def eadibitan(word):
  sylabs = []
  while len(word) > 0:
    regex1 = r"(([^aeiou][aeiouy]+)([^aeiou][aeiouy]+))|(([^aeiou][aeiouy]+[^aeiou])([^aeiou][aeiouy]+))|(([^aeiou][aeiouy]+[^aeiou])([^aeiou]{2}[aeiouy]+))"
    regex2 = r"([^aeiou]{0,2}[aeiouy]{1,3}([^aeiou](?=[^aeiou]{2})|[^aeiou]?$|[^aeiou]??))"
    regex = regex1 + "|" + regex2
    syl = re.match(regex,word).groups()
    if syl[-2] is not None:
      sylabs.append(syl[-2])
      word = word[len(syl[-2]):]
    elif syl[1] is not None:
      sylabs.append(syl[1])
      word = word[len(syl[1]):]
    elif syl[4] is not None:
      sylabs.append(syl[4])
      word = word[len(syl[4]):]
    elif syl[7] is not None:
      sylabs.append(syl[7])
      word = word[len(syl[7]):]
  mod_sylabs = []
  for sylab in sylabs:
    if re.match(r"^([^aeiou])([^aeiou])([aeiouy])", sylab):
      sylab = re.sub(r"^([^aeiou])([^aeiou])([aeiouy])",r"\2\3\1",sylab, count=1)
    else:
      sylab = re.sub(r"^([^aeiou])([aeiouy])",r"\2\1",sylab, count=1)
    mod_sylabs.append(sylab)
  return "".join(mod_sylabs)

