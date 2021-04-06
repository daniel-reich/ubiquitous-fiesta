
import re
def syllabification(word):
  regex = r"[pbtdkgG?fvszSZxhcjmnrly][aAeiou][pbtdkgG?fvszSZxhcjmnrly]{,2}(?![aAeiou])"
  return ".".join(re.findall(regex,word))

