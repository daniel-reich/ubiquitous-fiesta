
import re
​
def vowel_links(txt):
 regex = re.compile(r"[aeiou]\s[aeiou]")
 if (regex.search(txt)):
   return True
 return False

