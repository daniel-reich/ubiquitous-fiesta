
import re
def haiku(string):
  regex = r"([^aeiouy ,]*[AEIOUYaeiouy]+[^aeiouy ,]*)"
  return ([len([syl for syl in re.findall(regex, line) if syl != "e" and syl != "es" and syl != "e's"]) for line in string.split("/")]) == [5,7,5]

